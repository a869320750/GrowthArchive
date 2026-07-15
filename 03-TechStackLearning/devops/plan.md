## 必须吃透的基础概念（分两大块，先搞懂再动手）
### 板块1：K8s 核心概念（区分「控制平面」「业务节点」「资源对象」三层）
#### 1）集群分层架构（你最容易理解，对标存储管控面）
1. 控制平面 Master：apiserver/etcd/controller-manager/scheduler 整体作用、选主机制、REST API核心设计
2. 工作节点 Worker：kubelet、containerd、kube-proxy 各自职责，对标你存储FSA本地代理
3. 客户端工具：kubectl 本质（翻译HTTP请求）、kubeconfig权限认证逻辑

#### 2）核心业务资源对象（声明式API核心，所有业务载体）
1. Pod：最小运行单元，容器载体、生命周期、探针（存活/就绪）
2. 控制器（自愈核心）：Deployment无状态、StatefulSet有状态、DaemonSet节点常驻程序（对标FSA）
3. Service & kube-proxy：固定访问入口、负载均衡，解决Pod IP漂移
4. 配置管理：ConfigMap（普通配置）、Secret（密码/镜像密钥，DevOps高频）
5. 存储：PV/PVC持久化，对应你存储池抽象，对接GitLab/Jenkins持久数据
6. API Group/版本：为什么分多组、alpha/beta稳定版本，对应你们产品模块版本管控

#### 3）云原生配套概念（CI/CD必用）
1. 容器镜像：Dockerfile、私有镜像仓库（Harbor）、镜像分层缓存
2. Namespace：资源隔离，区分测试/生产、不同团队流水线
3. 资源配额 requests/limits：防止编译任务打满服务器，工程效能刚需
4. 临时一次性Job/CronJob：定时任务、一次性构建任务

### 板块2：Jenkins + DevOps 核心概念（和K8s联动重点）
1. Jenkins Master/Agent架构：Master调度、Agent执行，Agent=GitLab Runner的等价角色
2. 两种流水线：声明式Jenkinsfile（推荐，存代码仓库）、脚本式流水线
3. K8s动态Agent核心逻辑：插件如何调用K8s API、临时Pod生命周期（构建创建，完成销毁）
4. 凭证管理：账号、Git密钥、镜像仓库密码、集群证书（企业安全规范）
5. WebHook：GitLab提交代码自动触发Jenkins构建，自动化流水线入口
6. 制品链路：构建产物、镜像推送、环境部署、流水线日志持久化

### 板块3：DevOps工程效能底层思想（拔高主线认知）
1. 声明式管理 vs 命令式操作（K8s/YAML核心设计思想）
2. 环境一致性：镜像标准化，消除“本地能跑线上不行”
3. 弹性算力：闲置资源回收、高峰期扩容，提升服务器利用率
4. 自动化闭环：代码提交→自动测试→自动打包→自动部署，减少人工介入

# 4阶段完整学习落地路线（从概念→搭建→业务迁移→优化沉淀，边学边实战）
## 阶段1：基础概念理论学习（3~5天，只搞懂原理，不做复杂部署）
### 学习目标
不堆砌命令，先建立分布式系统框架，把K8s控制平面和你熟悉的OceanStor管控面对标理解，分清每个组件解决什么问题。
### 学习内容
1. 优先看 K8s 官方中文文档「概念板块」，跳过实操流水账书籍
   - 集群架构、控制平面各组件作用、etcd存储、控制器调谐循环（重点）
   - Pod、Deployment、Service、Secret、PVC 基础资源释义
2. 配套理解Docker基础：镜像、容器、Dockerfile（K8s的运行载体，不用深挖Docker底层）
3. Jenkins基础概念：Master/Agent、流水线、WebHook、凭证管理，分清和GitLab CI的区别
### 阶段小实战
用kind在你的12号Linux服务器搭**单机融合K8s集群**（一条命令完成，Master+Worker同机）
- 熟练kubectl基础命令：create/get/describe/logs/delete
- 手动创建Deployment跑一个Nginx，观察控制器自动重建Pod，直观感受自愈能力

## 阶段2：K8s深度实操（7~10天，吃透所有CI/CD需要用到的能力）
### 学习目标
掌握所有支撑Jenkins流水线的K8s能力，能独立编写YAML资源文件，理解REST资源模型
### 学习清单
1. 资源定义：手写yaml创建Deployment、Service、ConfigMap、Secret，理解声明式API
2. 持久化存储PV/PVC：模拟Jenkins、GitLab数据持久化，防止删除Pod丢失配置/缓存
3. 资源限制：给Pod配置CPU/内存requests/limits，理解资源隔离（解决编译抢占资源痛点）
4. Job一次性任务：理解临时构建Pod的生命周期（Jenkins K8s Agent底层就是Job）
5. 私有镜像仓库：部署简易Harbor，本地存储编译镜像，解决内网拉取速度问题
### 阶段实战
1. 在单机kind集群部署一套简易Harbor镜像仓库
2. 打包一个基础编译镜像（包含Go/JDK/Node等你们业务编译工具），推送到私有仓库
3. 手动创建Job Pod，拉取镜像模拟代码编译，构建完成自动销毁Pod

## 阶段3：Jenkins + K8s 联动落地（核心实战，10~15天，对接你现有GitLab业务）
### 学习目标
搭建完整自动化CI流水线，打通「GitLab代码仓库 → Jenkins → K8s动态Agent构建」，完成业务迁移
### 分步落地任务
1. 部署Jenkins主服务（两种方案可选）
   简易学习版：Docker运行Jenkins Master；长期生产版：部署为K8s StatefulSet
2. Jenkins核心配置学习
   - 安装Kubernetes插件、Git插件、凭证管理插件
   - 配置K8s集群连接信息（kubeconfig），编写Agent Pod模板（编译环境镜像、资源限制、缓存卷）
   - 配置GitLab WebHook，代码提交自动触发流水线
3. 编写标准Jenkinsfile（存放在代码仓库内，流水线即代码）
   流水线阶段：拉取代码→单元测试→编译打包→构建镜像→推送Harbor
4. 验证弹性能力：多次提交代码，观察K8s自动创建多个临时Agent Pod，构建结束自动销毁
5. 并行迁移现有业务：
   1）12号服务器Docker GitLab完整迁移11号老仓库数据
   2）新旧流水线并行跑，对比编译产物一致性
   3）验证稳定后，逐步下线原裸机GitLab与常驻Runner
### 关键学习点
- Jenkins Agent和GitLab Runner两套执行体系的差异、适用场景
- K8s动态Agent弹性伸缩带来的资源利用率提升
- Secret统一管理Git账号、镜像仓库密码，规范安全流程

## 阶段4：工程效能优化 & 沉淀（长期主线，拔高DevOps能力）
### 学习目标
从“能跑通流水线”升级为**标准化、可复用、提效的工程效能平台**，形成自己的落地经验
1. 流水线标准化：封装通用Jenkins共享库，统一多项目编译、打包逻辑，不用每个项目重复写脚本
2. 资源优化：编译缓存PVC、镜像分层优化构建速度、节点调度亲和性
3. 监控告警：K8s集群资源监控、Jenkins流水线失败告警、构建时长统计（效能量化）
4. 环境管理：基于K8s Namespace划分测试/预发环境，一键部署业务服务
5. 沉淀输出：整理完整落地文档、YAML模板、故障排错手册，作为DevOps实战项目履历

# 核心加分点
1. **底层平台能力+流程工具两手抓**
很多DevOps人员只会Jenkins流水线，不懂K8s底层调度；很多运维只会K8s不会CI编排，你同时吃透两套核心体系，求职/晋升竞争力极强。
2. 拥有完整企业级落地实战履历
不是测试环境玩具，是公司真实研发业务迁移，可完整复盘：资源弹性优化、旧业务割接、自动化流水线落地、研发效率提升数据，面试核心素材。
3. 贴合工程效能核心工作内容
工程效能核心就是：标准化交付流水线、算力资源池化、研发自动化、环境统一、降低人工运维成本，你整个项目刚好覆盖全部核心工作。
4. 形成分布式系统通用思维
存储管控面、K8s控制平面、CI调度平台底层都是「中心调度+节点代理+状态自愈」一套分布式设计范式，一通百通，后续学习云平台、服务网格、制品库都会更快。