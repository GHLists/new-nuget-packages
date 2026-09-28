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

## Latest list — 2026-09-28 09:23 UTC

New packages created between 2026-09-28 08:22 UTC and 2026-09-28 09:23 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T09-23-13-093241Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 08:29:06 | [SqlSugar.HGCore.Patched](https://www.nuget.org/packages/SqlSugar.HGCore.Patched) | 5.1.4.2-patch1 | YOUR-ORG-OR-NAME | Patched SqlSugar.HGCore 5.1.4.2 + matching SqlSugar core 5.1.4.196. Adds SqlSug… |
| 2026-09-28 09:10:16 | [NModbus.Extensions](https://www.nuget.org/packages/NModbus.Extensions) | 0.1.0 | xiapeng | 为 NModbus 提供的扩展方法和工具库 |
| 2026-09-28 09:15:20 | [Huddly.UsbDotNet.Hotplug](https://www.nuget.org/packages/Huddly.UsbDotNet.Hotplug) | 1.4.3 | Thomas Mittet | Async-streaming USB hotplug monitoring for UsbDotNet |
| 2026-09-28 09:15:22 | [Huddly.UsbDotNet.LibUsbNative](https://www.nuget.org/packages/Huddly.UsbDotNet.LibUsbNative) | 1.4.3 | Stian Myhre, Thomas Mittet | .NET wrapper for the libusb library |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
