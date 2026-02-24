tips1: 已经track的文件不受到.gitignore的限制。只要文件在index里，就会监控他的变化。
*也就是在创建或者更新.gitignore之前，已经把改文件提交到了暂存区*
methods：```
```
git rm --cached .obsidian/workspace-mobile.json //从暂存区移除

git commit -m "stop tracking workspace-mobile.json" //提交这个更改

//cat .git ignore 查看里面确实有这个文件
```
 
tips2： 每次都要重新输入账号密码
methos：
```
git config --global credential.helper store
//已经验证可行s



​原理： 这个命令会让 Git 把你下一次输入的账号密码以明文形式保存在本地文件（~/.git-credentials）中。  
​操作： 输入完这条命令后，再执行一次 git push，最后一次手动输入账号密码，以后 Git 就会自动读取了。
```

 



tips3: termux 类别
1. 切换镜像网站`termux-change-repo`
2. `pkg update && pkg upgrade -y`
3.  chagne