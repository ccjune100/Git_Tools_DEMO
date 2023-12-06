pytest -v
git add .
echo "Enter a commit message: "
read commitComment
git commit -m "$commitComment"
echo "what branch should the commit be pushed to?"
read branch
git push origin "$branch"