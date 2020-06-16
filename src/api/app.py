from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import db
from github import Github

app = Flask(__name__)
api = Api(app)

# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

temp_repos = ["kubernetes/kubernetes", "apache/spark"]

# top_repos = ["kubernetes/kubernetes", "apache/spark", "Microsoft/vscode",
#              "nodejs/node", "tensorflow/tensorflow", "freeCodeCamp/freeCodeCamp",
#              "apple/swift", "rust-lang/rust", "openshift/origin", "ansible/ansible"]

parser = reqparse.RequestParser()
parser.add_argument('task')

# Refresh: 
# Clears DB and saves last 3 days of data for given repos
class Refresh(Resource):
    def put(self):
        g = Github("9e338f1b517471deb0668bdda7b3b3c8ac7a3656")
        repos = [g.get_repo(repo) for repo in li]
        pulls_paginatedLists = dict((repo.name, repo.get_pulls(state="all")) for repo in repos)

        limit = date.today() - timedelta(3)
        repo_names = list(pulls_paginatedLists.keys())
        pulls_pls_3day = dict((name,[]) for name in repo_names)

        for repo in repo_names:
            for pull in pulls_paginatedLists[repo]:
                pull_date = pull.created_at.date()
                if pull_date == date.today():
                    continue
                elif pull_date >= limit:
                    pulls_pls_3day[repo].append(pull)
                else: 
                    break

        return pulls_pls_3day

api.add_resource(Refresh, '/api/refresh')

if __name__ == '__main__':
    # DISABLE DEBUG FOR PRODUCTION
    app.run(debug=True)

# # Todo
# # shows a single todo item and lets you delete a todo item
# class Todo(Resource):
#     def get(self, todo_id):
#         # abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]

#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201


# # TodoList
# # shows a list of all todos, and lets you POST to add new tasks
# class TodoList(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201

# ##
# ## Actually setup the Api resource routing here
# ##
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')