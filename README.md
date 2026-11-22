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

## Latest list — 2026-11-22 12:20 UTC

New packages created between 2026-11-22 11:20 UTC and 2026-11-22 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T12-20-41-53958Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 11:27:36 | [Maomi.MQ.RabbitMQ.Mediator](https://www.nuget.org/packages/Maomi.MQ.RabbitMQ.Mediator) | 2.4.0 | Maomi.MQ.RabbitMQ.Mediator | RabbitMQ Publisher and consumer communication model framework. |
| 2026-11-22 11:33:39 | [JeffTian.Id6Mail.Mcp](https://www.nuget.org/packages/JeffTian.Id6Mail.Mcp) | 0.1.0 | Jeff Tian | Local stdio MCP server that lets AI agents search and read the signed-in user's… |
| 2026-11-22 11:42:06 | [Shields.UI.Testing](https://www.nuget.org/packages/Shields.UI.Testing) | 1.0.0 | Martin Shields | Design checks for apps built on Shields.UI: the kit's tokens, tokens-only, cont… |
| 2026-11-22 11:42:07 | [Shields.UI](https://www.nuget.org/packages/Shields.UI) | 1.0.0 | Martin Shields | Shared design tokens, base styles and components for the Calorie Tracker and Wo… |
| 2026-11-22 11:43:18 | [Supprocom.JSONColdStore](https://www.nuget.org/packages/Supprocom.JSONColdStore) | 0.1.1 | mkn8rn | Commercial or AGPL-3.0. EF Core provider foundation for durable local JSON cold… |
| 2026-11-22 11:44:17 | [Maomi.Core.Aot](https://www.nuget.org/packages/Maomi.Core.Aot) | 2.4.0 | Maomi.Core.Aot | Maomi 框架的 AOT 版本，使用 Roslyn 源生成器在编译期完成模块化分析和依赖注入注册，适用于 NativeAOT 与裁剪发布，运行时零反射。 |
| 2026-11-22 11:57:30 | [Tinos.Api.Shell](https://www.nuget.org/packages/Tinos.Api.Shell) | 1.0.0-alpha | Tinos API contributors | The shell component for Tinos.Api |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
