import requests

requests.request("post", "https://cloud.robocorp.com/api/v1/workspaces/40c5a482-fc45-483a-9916-537e57169e9f/work-items", headers={
  "Content-Type": "application/json",
  "Authorization": "RC-WSKEY c5ZNO5fCMz0UHvLA0aedmsbqtT3etRzksn2h6rzsuzfOvZptMJacb38umWxEwjPRdK47eFTLpiTqxt6Jq0glF7RG9bTS6sxLG5R9WYvC2tgnWvc4BzGsdBnhICqwzHWgo"
}, json={"process":{"id":""},"payload":{"phrase":"israel", "topic":"war", "website":"https://news.yahoo.com/"}})