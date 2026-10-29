# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 15:22 UTC

New packages created between 2026-10-29 14:19 UTC and 2026-10-29 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T15-22-04-168893Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 14:23:38 | [Snail.Sdk.Mcp.JobClient](https://www.nuget.org/packages/Snail.Sdk.Mcp.JobClient) | 0.4.0 | orldev | The client side of a Snail MCP server's jobs: a long operation started by a too… |
| 2026-10-29 14:29:04 | [Soenneker.Blazor.Extensions.IJSObjectReferences](https://www.nuget.org/packages/Soenneker.Blazor.Extensions.IJSObjectReferences) | 11.0.2 | Jake Soenneker | Extension methods for IJSObjectReference that add operation context to JavaScri… |
| 2026-10-29 14:31:56 | [Nash.AzEnvPull](https://www.nuget.org/packages/Nash.AzEnvPull) | 1.0.1 | Jayson Nacional | CLI tool for extracting Azure App Service configurations. |
| 2026-10-29 14:34:41 | [Radzen.Factory.Client](https://www.nuget.org/packages/Radzen.Factory.Client) | 0.1.0 | Radzen | The client side of the apps Radzen Factory builds: data, identity and attachmen… |
| 2026-10-29 14:34:41 | [Radzen.Factory.Server](https://www.nuget.org/packages/Radzen.Factory.Server) | 0.1.0 | Radzen | The server side of the apps Radzen Factory builds: AddRadzenFactory, the base c… |
| 2026-10-29 14:40:13 | [Orbyss.Foundation.Web.DynamicPages](https://www.nuget.org/packages/Orbyss.Foundation.Web.DynamicPages) | 0.3.11 | Orbyss | Optional request-resolved application pages with bounded rendering and fresh co… |
| 2026-10-29 14:53:11 | [victor-wiki.PyException](https://www.nuget.org/packages/victor-wiki.PyException) | 1.0.0 | PyException | Collection of classes with the same name as Python exception class. |
| 2026-10-29 14:59:56 | [Wikandoo.SKM.Licensing](https://www.nuget.org/packages/Wikandoo.SKM.Licensing) | 8.1.0-beta0002 | Wikandoo | Wikandoo SKM - Clé de licence de 25 caractères par poste (sceau HMAC), scellé d… |
| 2026-10-29 15:01:11 | [Mud.Wechat.OfficialAccount.Callback](https://www.nuget.org/packages/Mud.Wechat.OfficialAccount.Callback) | 1.0.0 | Mud Studio | 微信公众号/服务号 SDK 回调接收包：URL 验证（GET echostr 回显）、消息推送（明文/兼容/安全三模式）、双验签（GET signature… |
| 2026-10-29 15:01:12 | [Mud.Wechat.Pay](https://www.nuget.org/packages/Mud.Wechat.Pay) | 1.0.0 | Mud Studio | 微信支付 SDK：商户配置面、签名/验签与加解密端口、平台证书存储端口、通知信封、官方错误码与异常（以上原 Abstractions 面）、APIv3 与 A… |
| 2026-10-29 15:01:12 | [Mud.Wechat.OpenTelemetry](https://www.nuget.org/packages/Mud.Wechat.OpenTelemetry) | 1.0.0 | Mud Studio | Mud.Wechat OpenTelemetry 适配包，一键开启微信 SDK 的分布式追踪与指标采集，自动注册 Wechat ActivitySource、… |
| 2026-10-29 15:01:13 | [Mud.Wechat.Pay.Callback](https://www.nuget.org/packages/Mud.Wechat.Pay.Callback) | 1.0.0 | Mud Studio | 微信支付 APIv3 SDK 回调接收包：平台证书验签、时间戳窗口闸、抗重放指纹、AEAD_AES_256_GCM resource 解密、通知分发与应答（{… |
| 2026-10-29 15:01:14 | [Mud.Wechat.Abstractions](https://www.nuget.org/packages/Mud.Wechat.Abstractions) | 1.0.0 | Mud Studio | Mud.Wechat 跨产品线公用横切层：响应判错契约、AppKey 形状校验、域名与 SSRF 白名单常量、配置基座、令牌持久化端口、errcode 令牌失… |
| 2026-10-29 15:01:14 | [Mud.Wechat.Work.AI.Mcp](https://www.nuget.org/packages/Mud.Wechat.Work.AI.Mcp) | 1.0.0 | Mud Studio | 企业微信线 AI 工具面的 MCP（Model Context Protocol）协议层：把已策展的受控工具面以 JSON-RPC 2.0 暴露为 MCP s… |
| 2026-10-29 15:01:15 | [Mud.Wechat.OfficialAccount](https://www.nuget.org/packages/Mud.Wechat.OfficialAccount) | 1.0.0 | Mud Studio | 微信公众号/服务号 SDK：认证与多应用基座（接口调用凭据签发、令牌管理器普通/稳定双通道、多公众号管理、配置面、常量/枚举/异常、回调信封与载荷契约）、官方… |
| 2026-10-29 15:01:16 | [Mud.Wechat.Redis](https://www.nuget.org/packages/Mud.Wechat.Redis) | 1.0.0 | Mud Studio | 企业微信 SDK Redis 分布式存储扩展包：令牌持久层（含批量删除）、企业授权仓储、套件票据仓储与回调抗重放守卫的 Redis 实现，适用于多实例部署，支… |
| 2026-10-29 15:01:16 | [Mud.Wechat.Work.AI](https://www.nuget.org/packages/Mud.Wechat.Work.AI) | 1.0.0 | Mud Studio | 企业微信线 AI Agent 底座：WechatAgent（ObservedDelegatingAgent 承载 ChatClientAgent、实现 IAg… |
| 2026-10-29 15:01:17 | [Mud.Wechat.Channels](https://www.nuget.org/packages/Mud.Wechat.Channels) | 1.0.0 | Mud Studio | 微信小店/视频号（channels 生态）SDK：配置面 ChannelsAppConfig、令牌类型/管理器（Wechat.Channels.AccessT… |
| 2026-10-29 15:01:18 | [Mud.Wechat.OpenPlatform](https://www.nuget.org/packages/Mud.Wechat.OpenPlatform) | 1.0.0 | Mud Studio | 微信开放平台「第三方平台」（component）SDK：component_verify_ticket 存储端口、component_access_token… |
| 2026-10-29 15:01:19 | [Mud.Wechat.Work.Callback](https://www.nuget.org/packages/Mud.Wechat.Work.Callback) | 1.0.0 | Mud Studio | 企业微信 SDK 回调接收包：URL 验证（GET echostr 回显）、suite_ticket / 授权事件推送与通讯录变更、异步任务完成通知的验签、A… |
| 2026-10-29 15:01:19 | [Mud.Wechat.AI](https://www.nuget.org/packages/Mud.Wechat.AI) | 1.0.0 | Mud Studio | 微信生态 AI 共享层（跨七线）：契约面 —— 工具身份轴 WechatToolPrincipal / 风险词表 WechatToolRiskVocabula… |
| 2026-10-29 15:01:20 | [Mud.Wechat.Channels.Callback](https://www.nuget.org/packages/Mud.Wechat.Channels.Callback) | 1.0.0 | Mud Studio | 微信小店/视频号（channels 生态）SDK 回调接收包：URL 验证（GET echostr 回显）、msg_signature 验签、AES 解密（官… |
| 2026-10-29 15:01:21 | [Mud.Wechat.Work.AI.Tools](https://www.nuget.org/packages/Mud.Wechat.Work.AI.Tools) | 1.0.0 | Mud Studio | 企业微信线 AI 工具面：WechatToolProfile（Mud.AI.Generator 剖面）、工具风险枚举与绑定类型、只读工具的策展声明（Curat… |
| 2026-10-29 15:01:22 | [Mud.Wechat.Ads](https://www.nuget.org/packages/Mud.Wechat.Ads) | 1.0.0 | Mud Studio | 腾讯广告（Tencent Ads） Marketing API v3.0 SDK：应用配置面与 OAuth 凭据端口、官方错误码与异常、全部出入参 DTO（A… |
| 2026-10-29 15:01:23 | [Mud.Wechat.MiniProgram](https://www.nuget.org/packages/Mud.Wechat.MiniProgram) | 1.0.0 | Mud Studio | 微信小程序 SDK：官方错误码与线级异常、业务声明式客户端（登录/二维码链接/内容安全/数据分析/订阅消息/XPay/云服务/直播/硬件设备 等 21 个业务… |
| 2026-10-29 15:02:00 | [cliopack.any](https://www.nuget.org/packages/cliopack.any) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:02 | [cliopack.linux-arm64](https://www.nuget.org/packages/cliopack.linux-arm64) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:04 | [cliopack.linux-x64](https://www.nuget.org/packages/cliopack.linux-x64) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:07 | [cliopack.osx-arm64](https://www.nuget.org/packages/cliopack.osx-arm64) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:08 | [cliopack.osx-x64](https://www.nuget.org/packages/cliopack.osx-x64) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:10 | [cliopack.win-x64](https://www.nuget.org/packages/cliopack.win-x64) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:02:11 | [cliopack](https://www.nuget.org/packages/cliopack) | 0.1.0 | ArchEmperor | TUI for pulling packages from Creatio environments via clio |
| 2026-10-29 15:10:38 | [Identisure.Client](https://www.nuget.org/packages/Identisure.Client) | 0.1.0 | Identisure | C# client for the Identisure REST API |
| 2026-10-29 15:13:23 | [Ruvio.Extensions.Idempotency](https://www.nuget.org/packages/Ruvio.Extensions.Idempotency) | 0.1.0 | Salih Cantekin | Run work once per key outside HTTP (message consumers, background jobs, gRPC) w… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
