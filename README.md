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

## Latest list — 2026-10-21 05:20 UTC

New packages created between 2026-10-21 04:20 UTC and 2026-10-21 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T05-20-08-365203Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 04:44:35 | [NyaXZ](https://www.nuget.org/packages/NyaXZ) | 1.0.0 | Alexey Sonkin | .NET XZ (LZMA2) compress/decompress library |
| 2026-10-21 04:50:06 | [Bitzsoft.Integrations.Translation.Abstractions](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.Abstractions) | 1.0.0 | Bitzsoft | 翻译服务抽象层 — 统一 ITranslationProvider / IAiTranslationProvider 接口、领域错误码与 11 家多供应商工厂… |
| 2026-10-21 04:58:37 | [Stellaegis.Trash.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Trash.PostgreSQL) | 5.0.0 | FRi | PostgreSQL store for Stellaegis.Trash (schema trash): items per compartment or… |
| 2026-10-21 04:58:37 | [Stellaegis.Trash.AspNetCore](https://www.nuget.org/packages/Stellaegis.Trash.AspNetCore) | 5.0.0 | FRi | ASP.NET Core endpoints for Stellaegis.Trash: put, list, read, restore and delet… |
| 2026-10-21 04:58:37 | [Stellaegis.Trash](https://www.nuget.org/packages/Stellaegis.Trash) | 5.0.0 | FRi | A generic trash for an application: a serialized object goes in with its identi… |
| 2026-10-21 05:00:38 | [Archie](https://www.nuget.org/packages/Archie) | 0.0.1 | Mattias Sundström | Architecture rules for .NET, enforced at compile time by Roslyn analyzers. |
| 2026-10-21 05:00:40 | [Robbiblubber.Util.ConsoleToolkit](https://www.nuget.org/packages/Robbiblubber.Util.ConsoleToolkit) | 1.0.9 | Alexander Lang | The robbiblubber.org Console Utility Library provides console application utili… |
| 2026-10-21 05:02:19 | [Bitzsoft.Integrations.Translation.Aliyun](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.Aliyun) | 1.0.0 | Bitzsoft | 阿里云机器翻译（alimt）实现 — 专业版 / 通用版 Translate，POP RPC v1 HMAC-SHA1 签名，支持 auto 源语言检测 |
| 2026-10-21 05:05:31 | [RuleScript.LanguageServer](https://www.nuget.org/packages/RuleScript.LanguageServer) | 0.2.0 | Mick | Language Server Protocol server for RuleScript (.rules) files. |
| 2026-10-21 05:07:13 | [Bitzsoft.Integrations.Translation.Baidu](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.Baidu) | 1.0.0 | Bitzsoft | 百度翻译开放平台实现 — 通用翻译 API（AppId + 密钥 MD5 签名），支持 auto 源语言与批量顺序翻译 |
| 2026-10-21 05:09:54 | [LabelTool](https://www.nuget.org/packages/LabelTool) | 1.0.0 | GreatBear | WinForms 深度学习图像标注用户控件：seg 语义分割多边形、det 多边形/点/圆、负样本标记、缩略图三态进度，标注自动保存到 PNG tEXt 块（… |
| 2026-10-21 05:12:12 | [Bitzsoft.Integrations.Translation.Tencent](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.Tencent) | 1.0.0 | Bitzsoft | 腾讯云机器翻译（TMT）实现 — TextTranslate / TextTranslateBatch / TextDetect，TC3-HMAC-SHA25… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
