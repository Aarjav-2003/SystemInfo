# SystemInfo

<p>This script gathers and displays various pieces of information about the system, including architecture, network name, OS details, processor details, and memory information. It uses multiple libraries (platform, psutil, cpuinfo, and wmi) to achieve this, each serving a specific purpose. The script also includes a mechanism to wait for user input before terminating.</p>

<h2>Importing Libraries</h2>
<ul>
  <li><b>platform:</b> Provides information about the underlying platform (operating system, architecture, etc.).</li>
  <li><b>psutil:</b> A cross-platform library for retrieving information on system utilization (CPU, memory, disks, network, sensors).</li>
  <li><b>cpuinfo:</b> Retrieves detailed information about the CPU.</li>
  <li><b>wimi:</b> Provides access to Windows Management Instrumentation (WMI) to get detailed information about Windows systems.</li>
</ul>

<p>When explaining this on paper, you can outline each section, describe the purpose of each library and function, and provide examples of the output for better understanding.</p>
