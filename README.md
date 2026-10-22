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

## Latest list — 2026-10-22 09:20 UTC

New packages created between 2026-10-22 08:21 UTC and 2026-10-22 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T09-20-00-618723Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 08:22:50 | [SemanticMapper.Jev](https://www.nuget.org/packages/SemanticMapper.Jev) | 0.1.1 | Akbar Dizaji | TypeSafe Jev semantic field matcher for SemanticMapper. Calls the TypeSafe Syst… |
| 2026-10-22 08:26:50 | [DWIS.RigOS.Capabilities.SOE.Model](https://www.nuget.org/packages/DWIS.RigOS.Capabilities.SOE.Model) | 1.0.1 | Eric Cayeux | Package Description |
| 2026-10-22 08:27:19 | [DWIS.RigOS.Capabilities.Controller.Model](https://www.nuget.org/packages/DWIS.RigOS.Capabilities.Controller.Model) | 1.0.4 | Eric Cayeux | Package Description |
| 2026-10-22 08:27:30 | [DWIS.RigOS.Capabilities.FDIR.Model](https://www.nuget.org/packages/DWIS.RigOS.Capabilities.FDIR.Model) | 0.0.2 | Eric Cayeux | Package Description |
| 2026-10-22 08:27:34 | [DWIS.RigOS.Capabilities.Procedure.Model](https://www.nuget.org/packages/DWIS.RigOS.Capabilities.Procedure.Model) | 1.0.1 | Eric Cayeux | Package Description |
| 2026-10-22 08:39:28 | [DWIS.RigOS.Capabilities.Service.Model](https://www.nuget.org/packages/DWIS.RigOS.Capabilities.Service.Model) | 0.0.1 | Eric Cayeux | Package Description |
| 2026-10-22 08:50:30 | [FryWorld.Plugin.Circuit](https://www.nuget.org/packages/FryWorld.Plugin.Circuit) | 2.0.8 | PrashantUnity,Code Fry Dev | Interactive analog and digital circuit schematic CAD and real-time MNA simulati… |
| 2026-10-22 08:52:09 | [JvmBridge.Tool](https://www.nuget.org/packages/JvmBridge.Tool) | 26.10.22.4199 | void-community | The jvmbridge command: disassemble class files, preview what an agent's patches… |
| 2026-10-22 09:01:08 | [Xsl3.Build](https://www.nuget.org/packages/Xsl3.Build) | 1.0.0 | Xsl3 contributors | Compiles XSLT stylesheets ahead of time for Xsl3 (XslCompiledTransform.Load(Typ… |
| 2026-10-22 09:01:10 | [Xsl3.Cli](https://www.nuget.org/packages/Xsl3.Cli) | 1.0.0 | Xsl3 contributors | Command-line tool for Xsl3, the XSLT 3.0, XSLT 2.0 and XPath 3.1 processor for… |
| 2026-10-22 09:06:41 | [3CGroup.Core.Infrastructure.ApplicationLogging](https://www.nuget.org/packages/3CGroup.Core.Infrastructure.ApplicationLogging) | 1.0.11 | 3CGroup | Shared structured application logging primitives for 3CGroup services. |
| 2026-10-22 09:06:44 | [3CGroup.Core.Infrastructure.ApplicationLogging.AspNetCore](https://www.nuget.org/packages/3CGroup.Core.Infrastructure.ApplicationLogging.AspNetCore) | 1.0.11 | 3CGroup | ASP.NET Core correlation and request logging middleware for 3CGroup services. |
| 2026-10-22 09:06:46 | [3CGroup.Core.Infrastructure.ApplicationLogging.MassTransit](https://www.nuget.org/packages/3CGroup.Core.Infrastructure.ApplicationLogging.MassTransit) | 1.0.11 | 3CGroup | MassTransit consumer correlation and retry logging for 3CGroup services. |
| 2026-10-22 09:07:40 | [xsi.osx-arm64](https://www.nuget.org/packages/xsi.osx-arm64) | 1.11.0 | Alexandre Mutel | CodeAlta Desktop: a desktop workspace for agentic AI coding on your local proje… |
| 2026-10-22 09:08:03 | [xsi](https://www.nuget.org/packages/xsi) | 1.11.0 | Alexandre Mutel | CodeAlta Desktop: a desktop workspace for agentic AI coding on your local proje… |
| 2026-10-22 09:08:10 | [xsi.osx-x64](https://www.nuget.org/packages/xsi.osx-x64) | 1.11.0 | Alexandre Mutel | CodeAlta Desktop: a desktop workspace for agentic AI coding on your local proje… |
| 2026-10-22 09:10:04 | [Shells.TypeMapper](https://www.nuget.org/packages/Shells.TypeMapper) | 1.1.0 | Datamit | Class model mapper between entities in .NET. |
| 2026-10-22 09:10:27 | [VitalWatch.AspNetCore](https://www.nuget.org/packages/VitalWatch.AspNetCore) | 0.1.0 | CestnyTR | VitalWatch Hub için ASP.NET Core raporlayıcı — yakalanmamış hatalar, 5xx yanıtl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
