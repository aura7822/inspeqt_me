#!/bin/bash
set -e

if [ ! -d ".git" ]; then
    echo "Error! This folder isn't a Git repository"
    exit 1
fi
echo "Repository detected"

echo "Analysing status..."
git status

echo "Deploying modifications..."
git add .

COMMIT_MSG="❖ Feature enhancements on $(date '+%Y-%m-%d %H:%M:%S')"
echo "Committing..."
git commit -m "$COMMIT_MSG" || {
    echo "No changes to commit found"
    exit 0
}
echo "Pushing to Github (aura7822)..."
git push origin main

echo "Bravo! Your repo has been updated successfully"
