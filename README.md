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

## Latest list — 2026-11-28 07:19 UTC

New packages created between 2026-11-28 06:21 UTC and 2026-11-28 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T07-19-09-358788Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 06:23:40 | [Findx.Extensions.Notify](https://www.nuget.org/packages/Findx.Extensions.Notify) | 11.1.2026.1128 | Findx.Extensions.Notify | Findx消息通知扩展组件（企业微信群机器人/应用消息、钉钉群机器人、SMTP邮件、微信公众号模板消息） |
| 2026-11-28 06:23:48 | [Findx.Extensions.WorkflowCore](https://www.nuget.org/packages/Findx.Extensions.WorkflowCore) | 11.1.2026.1128 | Findx.Extensions.WorkflowCore | Findx工作流核心扩展模块 |
| 2026-11-28 06:43:22 | [NewLife.ML](https://www.nuget.org/packages/NewLife.ML) | 1.0.2026.1128-beta0… | 新生命开发团队 | Tabular machine learning for .NET: data frame, training contract, evaluation me… |
| 2026-11-28 06:43:24 | [NewLife.ML.LightGbm](https://www.nuget.org/packages/NewLife.ML.LightGbm) | 1.0.2026.1128-beta0… | 新生命开发团队 | LightGBM adapter for NewLife.ML: train binary/multiclass classification and reg… |
| 2026-11-28 07:06:21 | [Blasphemous.EditorMode](https://www.nuget.org/packages/Blasphemous.EditorMode) | 0.1.0 | NewbieElton | A Blasphemous 1 mod that adds an in-game editor mode to tweak level layout on t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
