# git操作Time Out
1. 设置全局代理
  git config --global http.proxy 127.0.0.1:1080
  git config --global https.proxy 127.0.0.1:1080
2. 取消全局代理
  git config --global --unset http.proxy
  git config --global --unset https.proxy
