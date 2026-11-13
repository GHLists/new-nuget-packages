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

## Latest list — 2026-11-13 17:20 UTC

New packages created between 2026-11-13 16:19 UTC and 2026-11-13 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T17-20-27-180569Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 16:19:27 | [AmgadRichTextArabic](https://www.nuget.org/packages/AmgadRichTextArabic) | 1.0.0 | Amgad Edward | Rich Text Editor for Blazor with Arabic and English support, image editing, HTM… |
| 2026-11-13 16:20:20 | [VirtoCommerce.MCP.Testing](https://www.nuget.org/packages/VirtoCommerce.MCP.Testing) | 3.1001.0 | VirtoCommerce.MCP.Testing | Test helpers for modules that add tools to the Virto Commerce MCP module: call… |
| 2026-11-13 16:30:26 | [Tubatools.AiJunkCleanup](https://www.nuget.org/packages/Tubatools.AiJunkCleanup) | 1.15.0 | 图吧工具箱 | 给 AI 助手增加「垃圾清理」模式：AI 只读扫描并给出带原因和风险的清单，插件解析后由用户逐项确认，默认只勾选低风险项目，确认后直接删除并显示近似进度。 |
| 2026-11-13 16:38:43 | [Procteye](https://www.nuget.org/packages/Procteye) | 2.1.0 | Procteye | Idiomatic .NET SDK for the Procteye Integrity API (proctoring sessions and Stan… |
| 2026-11-13 17:02:12 | [EasyGL](https://www.nuget.org/packages/EasyGL) | 1.0.0 | YourNameOrHandle | A zero-dependency C# OpenGL 2D/3D rendering library with an accessible 1-to-10… |
| 2026-11-13 17:10:11 | [Wavvon.Sdk.AspNetCore](https://www.nuget.org/packages/Wavvon.Sdk.AspNetCore) | 0.1.0 | The Wavvon contributors | Map a Wavvon app's webhook onto an ASP.NET Core minimal-API route. |
| 2026-11-13 17:10:12 | [Wavvon.Sdk](https://www.nuget.org/packages/Wavvon.Sdk) | 0.1.0 | The Wavvon contributors | Write programs (bots and apps) that talk to a Wavvon hub. |
| 2026-11-13 17:14:03 | [Voidwell.Common.Configuration.EntityFramework](https://www.nuget.org/packages/Voidwell.Common.Configuration.EntityFramework) | 1.1.0 | VoidwellLabs | Stores runtime-editable application configuration in an Entity Framework Core t… |
| 2026-11-13 17:14:04 | [Voidwell.Common.RateLimiting](https://www.nuget.org/packages/Voidwell.Common.RateLimiting) | 1.1.0 | VoidwellLabs | Per-client rate limiting for APIs, built on the ASP.NET Core rate limiter. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
