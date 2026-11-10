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

## Latest list — 2026-11-10 05:21 UTC

New packages created between 2026-11-10 04:20 UTC and 2026-11-10 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T05-21-10-146618Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 04:42:05 | [XHao.AspectCore](https://www.nuget.org/packages/XHao.AspectCore) | 10.0.12 | XHao.AspectCore | AspectCore 代理校验优化 |
| 2026-11-10 04:54:55 | [HAKICODE.Workbench.Plugin.Generation3D](https://www.nuget.org/packages/HAKICODE.Workbench.Plugin.Generation3D) | 1.0.2 | HAKICODE | Tạo ảnh và mô hình 3D có xương, chuyển động trên máy GPU nội bộ, từ trợ lý, gia… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
