<h1>Server Postmortem</h1>
<h2>Issue summary</h2>
<p>The issue happened when the application was inaccessible because the server hosting the load balancer had the ip address changed dynamically and did not match the ip address configured in the domain names Arecord.</p>
<h2>Timeline</h2>
<p>The issue was detected on monday 8th may, 2023 and the issue was detected once we ran the command ifconfig and checked the ip address doesn't match the previous server ip address and we came to the conclusion that it could be the cause.
</p>
<h3>Action taken </h3>
<ul>
    <li><p>At this point I had to check if the haproxy server was installed and configured properly to direct traffic to the web servers.
    </p></li>
     <li><p>Confirm the ssl configuration and make sure the cert file is available.
    </p></li>
     <li><p>Open the cpanel of the domain name provider  and configured the new ip address to the A Record.
    </p></li>
</ul>
<h2>Root Cause</h2>
<p>The root cause of the issue was an abrupt change in the ip address of the server which didn't allow access to the server at that specific ip address.
</p>
<h2>Corrective and Preventive measures</h2>
<p>The corrective and preventive measures to this problem are that the ip address to the server should be fixed and not dynamic to avoid future ip address changes.
</p>
