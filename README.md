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

## Latest list — 2026-11-17 03:19 UTC

New packages created between 2026-11-17 02:20 UTC and 2026-11-17 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T03-19-58-346265Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 02:25:16 | [ZlmSharp.Extra](https://www.nuget.org/packages/ZlmSharp.Extra) | 0.1.6 | ZlmSharp.Extra | Package Description |
| 2026-11-17 02:25:19 | [ZlmSharp.Media.AutoGen](https://www.nuget.org/packages/ZlmSharp.Media.AutoGen) | 0.1.6 | ZlmSharp.Media.AutoGen | Package Description |
| 2026-11-17 02:58:36 | [Cornhsu.XamlFit](https://www.nuget.org/packages/Cornhsu.XamlFit) | 0.1.0 | 許彧銘 (Cornhsu) | XamlFit — static text-fit audit for WPF XAML. Computes the pixel budget of ever… |
| 2026-11-17 03:09:18 | [Globe3D.Avalonia](https://www.nuget.org/packages/Globe3D.Avalonia) | 2.0.0 | daipeng0809 | 面向 Avalonia 的实时三维地球控件：影像瓦片、程序化星空、大气散射、区域与标注图层、三维标记点（支持 png/jpg/gif/svg 图标），支持鼠标… |
| 2026-11-17 03:10:35 | [PicoActor.EventStore.InMemory](https://www.nuget.org/packages/PicoActor.EventStore.InMemory) | 2026.9.0 | PicoActor.EventStore.InMemory | In-memory event store for PicoActor: thread-safe, per-actor serialized, with sn… |
| 2026-11-17 03:10:36 | [PicoActor.EventStore.Jsonl](https://www.nuget.org/packages/PicoActor.EventStore.Jsonl) | 2026.9.0 | PicoActor.EventStore.Jsonl | Durable JSONL event store for PicoActor: one file per aggregate, append-only wi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
