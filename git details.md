tips1: 已经track的文件不受到.gitignore的限制。只要文件在index里，就会监控他的变化。
*也就是在创建或者更新.gitignore之前，已经把改文件提交到了暂存区*
methods：```
```
git rm --cached .obsidian/workspace-mobile.json //从暂存区移除

git commit -m "stop tracking workspace-mobile.json" //提交这个更改

//cat .git ignore 查看里面确实有这个文件
```
