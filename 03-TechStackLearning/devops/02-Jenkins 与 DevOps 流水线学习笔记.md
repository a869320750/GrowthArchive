# Jenkins + K8s联动 DevOps 学习笔记
> 学习目标：打通 GitLab → Jenkins → K8s动态Agent完整CI流水线
> 业务落地目标：现有GitLab研发流水线迁移方案验证

## 一、Jenkins基础架构 Master / Agent
### 1. Master核心职责
- 任务调度、流水线管理、页面展示、凭证存储
- ⚠️生产不建议Master直接执行构建任务
- 📝【个人心得/类比】

### 2. Agent 代理节点（等价 GitLab Runner）
#### 2.1 Master与Agent通信协议 JNLP
- 通信方向：Agent主动长连接Master
- 和GitLab Runner主动轮询模型对比
- 📝【个人心得/类比】

#### 2.2 Agent多种运行形态
- 常驻虚拟机/容器Agent
- K8s动态临时Agent（重点掌握）
- 📝【个人心得/类比】

## 二、Jenkins流水线体系
### 1. 两种流水线语法
#### 1.1 脚本式流水线（废弃趋势，了解即可）
#### 1.2 声明式流水线 Jenkinsfile（推荐）
- pipeline、stage、steps 标准结构
- 并行构建、后置处理、失败捕获
- 📝【个人心得/类比】

### 2. 流水线即代码理念
- Jenkinsfile存放于代码仓库，和代码一同版本管理
- 📝【个人心得/类比】

## 三、K8s动态Agent核心原理（本次业务落地核心）
### 1. Kubernetes插件工作机制
- Jenkins通过kubeconfig连接K8s apiserver
- Pod模板定义：构建镜像、资源限制、存储卷、缓存
### 2. Agent Pod完整生命周期
- 流水线启动 → 创建Pod → 执行编译任务 → 任务结束销毁Pod
### 3. 常见问题：僵尸Pod堆积、构建缓存丢失
- 📝【个人心得/类比】

## 四、凭证管理体系
### 1. Jenkins内置凭证类型
- Git账号、SSH密钥、用户名密码、密钥文件
### 2. 安全规范：禁止明文硬编码在脚本内
- 📝【个人心得/类比】

## 五、GitLab WebHook 自动触发流水线（核心链路）
### 1. WebHook基础原理
- GitLab收到代码Push/MR → 主动POST HTTP请求通知Jenkins
### 2. 完整配置链路
- Jenkins：开启远程触发，生成安全Token
- GitLab仓库：配置WebHook地址、触发事件
### 3. 备选触发方式（不推荐）
- 轮询SCM、页面手动构建
- 📝【个人心得/类比】

## 六、完整制品链路
1. GitLab拉取源码
2. 单元测试、编译打包
3. 构建容器镜像
4. 推送镜像至Harbor私有仓库
5. （扩展）调用K8s API部署新版本服务
### 制品管理、日志持久化方案
- 📝【个人心得/类比】

## 七、Jenkins两种部署形态对比
1. Docker独立运行Jenkins Master（学习测试首选）
2. K8s StatefulSet托管Jenkins（长期生产方案）
- 📝【个人心得/类比】

## 八、实操任务清单
1. 部署Jenkins Master，安装K8s插件
2. 配置kubeconfig连通本机K8s集群
3. 编写Jenkinsfile，测试K8s动态Agent构建
4. 配置GitLab WebHook，实现代码提交自动触发构建
5. 完整跑通：代码提交 → 自动编译 → 镜像推送Harbor