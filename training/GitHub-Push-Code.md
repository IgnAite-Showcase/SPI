### How to Clone Push local code to Git Hub remote Repository.
- git clone'https://github.com/IgnAite-Showcase/IGN.git'
- Perform necessary Changes/Development

### Commit and push changes to Remote Repository.
- git config --global init.befaultBranch main
- git init -b main
- git add .
- git commit -m "commit to main branch"
- git remote add origin 'https://github.com/IgnAite-Showcase/IGN.git'
- git push -f -u origin main
