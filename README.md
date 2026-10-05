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

## Latest list — 2026-10-05 19:21 UTC

New packages created between 2026-10-05 18:21 UTC and 2026-10-05 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T19-21-31-925052Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 18:31:36 | [cap.dotnetdoctor](https://www.nuget.org/packages/cap.dotnetdoctor) | 1.1.0 | DotnetDoctor | A .NET global tool for diagnosing .NET development environments. |
| 2026-10-05 18:43:52 | [Menchul.GeoNames.org.MSSQL](https://www.nuget.org/packages/Menchul.GeoNames.org.MSSQL) | 3.0.0 | Ivan Perehynets | Package Description |
| 2026-10-05 18:43:53 | [Menchul.GeoNames.org.PostgreSQL](https://www.nuget.org/packages/Menchul.GeoNames.org.PostgreSQL) | 3.0.0 | Ivan Perehynets | Package Description |
| 2026-10-05 18:43:55 | [Menchul.GeoNames.org.SQLite](https://www.nuget.org/packages/Menchul.GeoNames.org.SQLite) | 3.0.0 | Ivan Perehynets | Package Description |
| 2026-10-05 18:47:32 | [Asteroid.Validation.CompilerTools](https://www.nuget.org/packages/Asteroid.Validation.CompilerTools) | 0.1.0 | Asteroid.Validation.CompilerT… | Source generator paired with Asteroid.Validation (registration-closure plan emi… |
| 2026-10-05 18:47:34 | [Asteroid.UiScene.CompilerTools](https://www.nuget.org/packages/Asteroid.UiScene.CompilerTools) | 0.1.0 | Asteroid.UiScene.CompilerTools | Source generator paired with Asteroid UiToolkit scene localization ([UiScene]/[… |
| 2026-10-05 18:47:55 | [JuffMa.Controls.Acrylic](https://www.nuget.org/packages/JuffMa.Controls.Acrylic) | 1.0.0 | Julian Rossbach | Simple and minimal acrylic/frosted glass controls for AvaloniaUI. |
| 2026-10-05 18:53:39 | [Novolis.Silk](https://www.nuget.org/packages/Novolis.Silk) | 2026.1.1.2 | Novolis | Novolis Silk — one install for GLFW/OpenGL hosts. Pins Silk.NET transitively. D… |
| 2026-10-05 18:53:40 | [Novolis.Silk.Capture](https://www.nuget.org/packages/Novolis.Silk.Capture) | 2026.1.1.2 | Novolis | OpenGL framebuffer readback for Novolis.Silk hosts (Rgba32 pixels). |
| 2026-10-05 18:53:41 | [Novolis.Silk.Compute](https://www.nuget.org/packages/Novolis.Silk.Compute) | 2026.1.1.2 | Novolis | Silk.NET Vulkan + Shaderc compute helpers over BCL/Math buffers. Does not refer… |
| 2026-10-05 18:53:42 | [Novolis.Silk.Game](https://www.nuget.org/packages/Novolis.Silk.Game) | 2026.1.1.2 | Novolis | Jam loop for Novolis.Silk — Run(title, size, update) with no scene types. |
| 2026-10-05 18:53:43 | [Novolis.Silk.Runtime](https://www.nuget.org/packages/Novolis.Silk.Runtime) | 2026.1.1.2 | Novolis | Silk.NET window, OpenGL context, input, planar quad batch, and CPU-pixel blit.… |
| 2026-10-05 18:54:14 | [Sharp.Tui](https://www.nuget.org/packages/Sharp.Tui) | 0.1.0 | Goshya | A small, dependency-free, NativeAOT-clean TUI framework for .NET built around T… |
| 2026-10-05 19:04:02 | [FT.AmoCRM](https://www.nuget.org/packages/FT.AmoCRM) | 1.0.3 | FT.AmoCRM contributors | .NET Standard client for the amoCRM API v4 with OAuth, typed CRM resources, fil… |
| 2026-10-05 19:07:35 | [replay.blackice.msgpack](https://www.nuget.org/packages/replay.blackice.msgpack) | 1.0.2 | replay | replay.re BlackICE Script SDK -- Visit docs.replay.re for more information |
| 2026-10-05 19:07:36 | [replay.blackice.shared](https://www.nuget.org/packages/replay.blackice.shared) | 1.0.2 | replay | replay.re BlackICE Script SDK -- Visit docs.replay.re for more information |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
