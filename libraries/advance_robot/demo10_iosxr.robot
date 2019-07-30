# Demo Script to verify sanity of network

*** Settings ***
# Importing test libraries, resource files and variable files.
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot


*** Variables ***
# Defining variables that can be used elsewhere in the test data. 
# Can also be driven as dash argument at runtime

# Define the pyATS testbed file to use for this run
${testbed}     virl_iosxr.yaml 

*** Test Cases ***
# Creating test cases from available keywords.


# ---------  Initilize -----------
Initialize
    # Initializes the pyATS/Genie Testbed
    # pyATS Testbed can be used within pyATS/Genie
    use genie testbed "${testbed}"

    # Connect to both device
    connect to device "uut"
    connect to device "helper"

Verify Ping from uut to helper
    run testcase    pyats_loopback_reachability.PingTestcase    device=uut
Verify Ping from helper to uut
    run testcase    pyats_loopback_reachability.PingTestcase    device=helper


# ---------  Verify counts of features -----------
# Verify Bgp Neighbors
Verify the counts of Bgp 'established' neighbors for uut&helper
    verify count "10" "bgp neighbors" on device "uut"
    verify count "10" "bgp neighbors" on device "helper"

# Verify Bgp Routes
# Tags can be used to control the behavior of the tests, noncritical tests which
# fail, will not cause the entire job to fail

Verify the counts of Bgp routes for uut&helper
    [Tags]    noncritical
    verify count "10" "bgp routes" on device "uut"
    verify count "10" "bgp routes" on device "helper"

# Verify OSPF neighbor counts
Verify the counts of Ospf 'full' neighbors for uut&helper
    verify count "2" "ospf neighbors" on device "uut"
    verify count "2" "ospf neighbors" on device "helper"

# Verify Interfaces
Verify the counts of 'up' Interace for uut&helper
    verify count "19" "interface up" on device "uut"
    verify count "19" "interface up" on device "helper"


# ---------  Take snapshot before testcases -----------
Profile bgp & ospf on All
    Profile the system for "bgp;ospf" on devices "uut" as "snap1"


# ---------  Global verifications 1 -----------
verify Bgp summary before trigger UnconfigureBgpNeighbor
    Run verification "Verify_BgpInstanceSummary_vrf_type_all" on device "uut"
verify Bgp neighbors before trigger UnconfigureBgpNeighbor
    Run verification "Verify_BgpInstanceNeighborsDetail_vrf_type_all" on device "uut"


# ---------  Testcase 1 -----------
Testcase UnconfigureBgpNeighbor
    run testcase    pyats_loopback_reachability.DeleteBgpNeighbor    device=uut  number=1

# Verify Bgp Neighbors delete 1
Verify the counts of Bgp 'established' neighbors for uut&helper is deleted by 1 
    verify count "9" "bgp neighbors" on device "uut"
    verify count "9" "bgp neighbors" on device "helper"

Profile bgp & ospf on All after delete BGP neighbor 
    Profile the system for "bgp;ospf" on devices "uut" as "snap2"
    Compare profile "snap1" with "snap2" on devices "uut"

Recover the testbed
    run testcase    pyats_loopback_reachability.RestoreDevice    device=uut


# ---------  Global verifications 2 -----------
verify Bgp summary after trigger UnconfigureBgpNeighbor
    Run verification "Verify_BgpInstanceSummary_vrf_type_all" on device "uut"
verify Bgp neighbors after trigger UnconfigureBgpNeighbor
    Run verification "Verify_BgpInstanceNeighborsDetail_vrf_type_all" on device "uut"


# ---------  Testcase 2 -----------
# Verify Genie verifications/triggers test

Trigger UnconfigConfigBgp
    Run trigger "TriggerUnconfigConfigBgp" on device "uut" using alias "cli"


# ---------  Global verifications 3 -----------
verify Bgp summary after GENIE trigger UnconfigConfigBgp
    Run verification "Verify_BgpInstanceSummary_vrf_type_all" on device "uut"
verify Bgp neighbors after GENIE trigger UnconfigConfigBgp
    Run verification "Verify_BgpInstanceNeighborsDetail_vrf_type_all" on device "uut"


# ---------  Take snapshot and compare with the original one after testcases -----------
Profile bgp & ospf on All after
    Profile the system for "bgp;ospf" on devices "uut" as "snap3"
    Compare profile "snap3" with "snap1" on devices "uut"
