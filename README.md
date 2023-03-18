# MeshNetworkAnalysis
Approcah to detect mesh networks among other networks


# Creating Mesh Network
 <code>sudo service network-manager stop</code>
 <br/>
 <code>sudo ip link set wlo1 down</code>
 <br/>
<p>Configuration</p>
<br/>
<p>Switch the card into ad hoc mode</p>
<br/>
<code>sudo iwconfig wlo1 mode ad-hoc</code>
<br/>
<p>Select the channel number.</p>
<br/>
<code>sudo iwconfig wlo1 channel 1</code>
<br/>
<p>Add the name (ssid) for the network you want to create/join. Use single quotes if there is a space in the name.</p>
<br/>
<code>sudo iwconfig wlo1 essid Kavach</code>
<br/>
<p>Add a WEP encryption key</p>
<br/>
<code>sudo iwconfig wlo1 key 1234567890</code>
<br/>
<p>Set the nodes to the same cell number as the ad-hoc interface.</p>
<br/>
<code>sudo iwconfig wlo1 ap 12:3E:30:39:BE:A1</code>
<br/>
<p>Activation</p>
<br/>
<p>Bring the interface back up</p>
<br/>
<code>sudo ip link set wlo1 up</code>
<br/>
<p>If you want to do it manually, you will have to make up an IP address.</p>
<br/>
<code>sudo ip addr add 169.254.34.2/16 dev wlo1</code>
<br/>
<code>ping 169.254.34.2</code>
<br/>
<p>Source : </p>
<br/>
<p>https://bbs.archlinux.org/viewtopic.php?id=230151</p>
<br/>
<p>https://help.ubuntu.com/community/WifiDocs/Adhoc</p>
