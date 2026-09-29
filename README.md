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

## Latest list — 2026-09-29 16:22 UTC

New packages created between 2026-09-29 15:20 UTC and 2026-09-29 16:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T16-22-24-642784Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 15:22:21 | [Swevo.AutoAssert.Analyzers](https://www.nuget.org/packages/Swevo.AutoAssert.Analyzers) | 1.0.0 | Justin Bannister | Roslyn analyzers for AutoAssert that catch common fluent-assertion footguns at… |
| 2026-09-29 15:22:22 | [Swevo.AutoAssert.AspNetCore](https://www.nuget.org/packages/Swevo.AutoAssert.AspNetCore) | 1.0.0 | Justin Bannister | HTTP response assertions for AutoAssert: fluent, chainable assertions for HttpR… |
| 2026-09-29 15:22:26 | [Swevo.AutoAssert.Generator](https://www.nuget.org/packages/Swevo.AutoAssert.Generator) | 1.0.0 | Justin Bannister | Compile-time BeEquivalentTo comparer generator for AutoAssert. Mark a type with… |
| 2026-09-29 15:22:27 | [Swevo.AutoAssert.Json](https://www.nuget.org/packages/Swevo.AutoAssert.Json) | 1.0.0 | Justin Bannister | JSON assertions for AutoAssert: BeValidJson, HaveJsonProperty, and BeEquivalent… |
| 2026-09-29 15:25:17 | [AutoMap.Cli](https://www.nuget.org/packages/AutoMap.Cli) | 1.0.1 | Justin Bannister | CI verification tool for AutoMap.Generator — `dotnet automap verify` reflects i… |
| 2026-09-29 15:27:49 | [Amafu](https://www.nuget.org/packages/Amafu) | 4.4.4 | Rainer Burkhardt | Standalone cloud-storage discovery and RAIkeep configuration bootstrap CLI. |
| 2026-09-29 15:31:36 | [nanoFramework.Iot.Device.Vcnl4040](https://www.nuget.org/packages/nanoFramework.Iot.Device.Vcnl4040) | 1.0.1 | nanoframework | This package includes the VCNL4040 proximity and ambient light sensor binding f… |
| 2026-09-29 15:46:39 | [PlainKit.Blazor](https://www.nuget.org/packages/PlainKit.Blazor) | 0.9.0 | Plainkit contributors | Blazor components over Plainkit, the dependency-free HTML/CSS/JS toolkit. Ships… |
| 2026-09-29 15:51:04 | [NetForms.Platform](https://www.nuget.org/packages/NetForms.Platform) | 0.1.0 | NetForms contributors | Platform abstraction for NetForms: window, input, clipboard, native dialogs. No… |
| 2026-09-29 15:51:05 | [NetForms.ExtraControls](https://www.nuget.org/packages/NetForms.ExtraControls) | 0.1.0 | NetForms contributors | Extra controls for NetForms (Windows Forms for Windows and Linux): ToggleSwitch… |
| 2026-09-29 15:51:05 | [NetForms.Platform.Avalonia](https://www.nuget.org/packages/NetForms.Platform.Avalonia) | 0.1.0 | NetForms contributors | Avalonia 12 implementation of the NetForms platform layer: one Avalonia Window… |
| 2026-09-29 15:51:05 | [NetForms.Templates](https://www.nuget.org/packages/NetForms.Templates) | 0.1.0 | NetForms contributors | Project and item templates for NetForms, WinForms for Windows and Linux. |
| 2026-09-29 15:51:05 | [NetForms.Drawing.Common](https://www.nuget.org/packages/NetForms.Drawing.Common) | 0.1.0 | NetForms contributors | System.Drawing.Common type-forwarding facade of NetForms: code and resources th… |
| 2026-09-29 15:51:07 | [NetForms.Convert](https://www.nuget.org/packages/NetForms.Convert) | 0.1.0 | NetForms contributors | Moves a Windows Forms project to NetForms so it builds and runs on Linux: repor… |
| 2026-09-29 15:51:08 | [NetForms.Drawing](https://www.nuget.org/packages/NetForms.Drawing) | 0.1.0 | NetForms contributors | System.Drawing (Graphics, Font, Pen, Brush, Bitmap) implemented on SkiaSharp. |
| 2026-09-29 15:51:08 | [NetForms](https://www.nuget.org/packages/NetForms) | 0.1.0 | NetForms contributors | System.Windows.Forms, cross-platform: own Control tree, own painting via SkiaSh… |
| 2026-09-29 15:56:51 | [Darnelix.Webp](https://www.nuget.org/packages/Darnelix.Webp) | 1.1.0 | Darnelix | Darnelix.Webp is a pure-C#, dependency-free WebP codec: decode and encode lossy… |
| 2026-09-29 15:58:35 | [S7Sharp.Watch](https://www.nuget.org/packages/S7Sharp.Watch) | 1.1.1 | xibeiwind@126.com | S7Sharp 的数据变化监控库：按每个定义自己的刷新间隔周期读一块数据（定义来源可以是 C# 类，也可以是 JSON 配置生成的运行期类型）， 与缓存按字节… |
| 2026-09-29 15:59:31 | [Eigenverft.WebLib.SerilogRelayReceiver](https://www.nuget.org/packages/Eigenverft.WebLib.SerilogRelayReceiver) | 1.0.0.6 | Eigenverft | ASP.NET Core receiver for Eigenverft SerilogRelay batches with provider-neutral… |
| 2026-09-29 15:59:59 | [Darnelix.Webp.Cli](https://www.nuget.org/packages/Darnelix.Webp.Cli) | 1.1.0 | Darnelix | webpx is the command-line front end for Darnelix.Webp, a pure-C#, dependency-fr… |
| 2026-09-29 16:06:54 | [Eigenverft.NetLib.SerilogRelay](https://www.nuget.org/packages/Eigenverft.NetLib.SerilogRelay) | 0.1.0.26 | Eigenverft | Durable Serilog relay with local persistent spooling and restart-safe delivery. |
| 2026-09-29 16:14:17 | [Shenora.Chromium](https://www.nuget.org/packages/Shenora.Chromium) | 0.17.0 | Jiarong Gu | Shenora's Chromium engine, through CEF, for an app that ships its own browser e… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
