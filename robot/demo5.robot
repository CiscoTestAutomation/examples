# Demo Script to verify sanity of network

*** Settings ***
# Importing test libraries, resource files and variable files.
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot


*** Variables ***
# Defining variables that can be used elsewhere in the test data. 
# Can also be driven as dash argument at runtime

# Define the pyATS testbed file to use for this run
${testbed}     cisco_live.yaml 

*** Test Cases ***
# Creating test cases from available keywords.

Initialize
    # Initializes the pyATS/Genie Testbed
    # pyATS Testbed can be used within pyATS/Genie
    use genie testbed "${testbed}"

    # Connect to both device
    connect to device "nx-osv-1"
    connect to device "helper"
    
parser show bgp all detail
    ${output}=    parse "show version" on device "nx-osv-1"

Verify Ping from nx-osv-1 to helper
    run testcase     examples.genie.demo5_robot.pyats_loopback_reachability.NxosPingTestcase    device=nx-osv-1
Verify Ping from helper to nx-osv-1
    run testcase     examples.genie.demo5_robot.pyats_loopback_reachability.PingTestcase    device=helper

# Verify Bgp Neighbors
Verify the counts of Bgp 'established' neighbors for nx-osv-1&helper
    verify count "1" "bgp neighbors" on device "nx-osv-1"
    verify count "1" "bgp neighbors" on device "helper"

# Verify Bgp Routes
# Tags can be used to control the behavior of the tests, noncritical tests which
# fail, will not cause the entire job to fail

Verify the counts of Bgp routes for nx-osv-1&helper
    [Tags]    noncritical
    verify count "2" "bgp routes" on device "nx-osv-1"
    verify count "2" "bgp routes" on device "helper"

# Verify OSPF neighbor counts
Verify the counts of Ospf 'full' neighbors for nx-osv-1&helper
    verify count "2" "ospf neighbors" on device "nx-osv-1"
    verify count "2" "ospf neighbors" on device "helper"

# Verify Interfaces
Verify the counts of 'up' Interace for nx-osv-1&helper
    verify count "5" "interface up" on device "nx-osv-1"
    verify count "5" "interface up" on device "helper"

Profile bgp & ospf on nx-osv-1
    Profile the system for "ospf;config" on devices "nx-osv-1" as "snap1"

verify Bgp Nexthop Database before trigger sleep
    run verification "Verify_BgpAllNexthopDatabase" on device "nx-osv-1"

Trigger sleep
    run trigger "TriggerSleep" on device "nx-osv-1" using alias "cli"

verify Bgp Nexthop Database after trigger sleep
    run verification "Verify_BgpAllNexthopDatabase" on device "nx-osv-1"

Profile bgp & ospf on nx-osv-1, Compare it with previous snapshot
    Profile the system for "ospf;config" on devices "nx-osv-1" as "snap2"
    Compare profile "snap2" with "snap1" on devices "nx-osv-1"

