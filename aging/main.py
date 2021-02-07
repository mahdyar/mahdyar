import os
from github import Github
from datetime import date

# Get environment variables
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]

# Extract repository name because it's combined with username
repositoryName = GITHUB_REPOSITORY.split("/")[1]

bDay = date(2002, 1, 8)
today = date.today()

# Calculate age and cast to str
age = str(today.year - bDay.year -
          ((today.month, today.day) < (bDay.month, bDay.day)))

filePath = "README.md"

g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(repositoryName)

file = repo.get_contents(filePath)
content = file.decoded_content.decode()

if age not in content:
    templateFilePath = "aging/README.template.md"
    templateFile = repo.get_contents(templateFilePath)
    templateContent = templateFile.decoded_content.decode()

    newContent = templateContent.replace("{{ AGE }}", age)
    repo.update_file(filePath, "feat: hbday to me 🎉", newContent, file.sha)
