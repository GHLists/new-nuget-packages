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

## Latest list — 2026-09-29 00:20 UTC

New packages created between 2026-09-28 23:19 UTC and 2026-09-29 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T00-20-27-766314Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 23:20:21 | [SimpleSharpBLE](https://www.nuget.org/packages/SimpleSharpBLE) | 1.2.0 | The California Open Source Co… | .NET bindings for SimpleBLE. |
| 2026-09-28 23:41:37 | [Vestigium.Helpers.PerfMon](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon) | 0.1.1 | Vestigium | Shared performance sample contract, job runner, and counter source. |
| 2026-09-28 23:42:07 | [Vestigium.Helpers.PerfMon.Cpu](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.Cpu) | 0.1.1 | Vestigium | Processor PDH samples. |
| 2026-09-28 23:42:28 | [Vestigium.Helpers.PerfMon.Disk](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.Disk) | 0.1.1 | Vestigium | Physical and logical disk PDH samples. |
| 2026-09-28 23:42:56 | [Vestigium.Helpers.PerfMon.Gpu](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.Gpu) | 0.1.1 | Vestigium | GPU engine and adapter memory the OS exposes. |
| 2026-09-28 23:43:16 | [Vestigium.Helpers.PerfMon.Memory](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.Memory) | 0.1.1 | Vestigium | Commit, available, and machine memory samples. |
| 2026-09-28 23:43:37 | [Vestigium.Helpers.PerfMon.Network](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.Network) | 0.1.1 | Vestigium | Adapter PDH rates and errors. |
| 2026-09-28 23:44:27 | [Vestigium.Helpers.PerfMon.PageFile](https://www.nuget.org/packages/Vestigium.Helpers.PerfMon.PageFile) | 0.1.1 | Vestigium | Pagefile usage and paging samples. |
| 2026-09-28 23:47:37 | [Temporalio.Extensions.Gcp.CloudRun.Id](https://www.nuget.org/packages/Temporalio.Extensions.Gcp.CloudRun.Id) | 1.20.0 | Temporal | Temporal SDK .NET Google Cloud Run Identity Extension |
| 2026-09-28 23:48:11 | [Temporalio.Extensions.WorkflowStreams](https://www.nuget.org/packages/Temporalio.Extensions.WorkflowStreams) | 1.20.0 | Temporal | Experimental Workflow Streams extension for the Temporal .NET SDK |
| 2026-09-28 23:52:45 | [Mediarion.Streaming](https://www.nuget.org/packages/Mediarion.Streaming) | 0.4.0 | Mediarion contributors | Streaming requests for Mediarion: one request, many responses, arriving as they… |
| 2026-09-29 00:06:31 | [Microsoft.Azure.Iot.Device](https://www.nuget.org/packages/Microsoft.Azure.Iot.Device) | 2.0.0-preview | Microsoft | Device client SDK for connecting devices to Azure IoT hub and the Azure Device… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
