from diagrams import Diagram, Cluster
from diagrams.aws.general import General

# Custom color scheme
colors = {
    "ou_level1": "#4169E1",  # Royal Blue
    "ou_level2": "#FFD700",  # Gold
    "ou_level3": "#FF4500",  # Orange Red
    "account": "#228B22"     # Forest Green
}

with Diagram("AWS Landing Zone Account Structure", show=False, direction="TB"):
    with Cluster("Root"):
        root = General("Root", **{"fillcolor": colors["ou_level1"]})

        with Cluster("OU Level 1"):
            ou_sandbox = General("Sandbox", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    ou_sandbox_norestrictvpc = General("NoRestrictVPC", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_tcvv_sandbox = General("DEA-TCVV-Sandbox", **{"fillcolor": colors["account"]})
                    ou_sandbox_restrictvpc = General("RestrictVPC", **{"fillcolor": colors["ou_level3"]})

            ou_security = General("Security", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    with Cluster("Account Level"):
                        account_dea_security = General("DEA Security", **{"fillcolor": colors["account"]})
                        account_log_archive = General("Log Archive", **{"fillcolor": colors["account"]})

            ou_infrastructure = General("Infrastructure", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    with Cluster("Account Level"):
                        account_dea_stratus_mgn_staging = General("DEA-Stratus-MGN-Staging", **{"fillcolor":colors["account"]})
                        account_network = General("Network", **{"fillcolor":colors["account"]})
                        account_shared_services = General("Shared Services", **{"fillcolor":colors["account"]})
                        account_dea_workspaces_test = General("DEA-Workspaces-Test", **{"fillcolor":colors["account"]})
                        account_dea_workspaces = General("DEA-Workspaces", **{"fillcolor":colors["account"]})

            ou_tenants = General("Tenants", **{"fillcolor": colors["ou_level1"]})

            # Example: Adding a Level 2 OU and an account under Tenants
            with Cluster("OU Level 2"):
                ou_sod = General("SOD", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_sod_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    ou_sod_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

                ou_datalakes = General("Datalakes", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_datalakes_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    ou_datalakes_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

                ou_intel = General("Intel", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_intel_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

                    # Example: Adding an account under a Level 3 OU
                    with Cluster("Account Level"):
                        account_dea_concorde_prod = General("DEA-Concorde-Prod", **{"fillcolor": colors["account"]})
                        account_dea_speedwayu_mig_prod = General("DEA-SpeedwayU-Mig-Prod", **{"fillcolor": colors["account"]})
                        account_dea_ctt_prod = General("DEA-CTT-Prod", **{"fillcolor": colors["account"]})
                        account_mos_prod = General("DEA-MOS-Prod", **{"fillcolor": colors["account"]})

                    ou_intel_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_concorde_pre_prod = General("DEA-Concorde-PreProd", **{"fillcolor": colors["account"]})
                        account_dea_speedwayu_mig_non_prod = General("DEA-SpeedwayU-Mig-NonProd", **{"fillcolor": colors["account"]})
                        account_dea_ctt_non_prod = General("DEA-CTT-NonProd", **{"fillcolor": colors["account"]})
                        account_dea_concorde_test = General("DEA-Concorde-Test", **{"fillcolor": colors["account"]})
                        account_mos_dev = General("DEA-MOS-Dev", **{"fillcolor": colors["account"]})
                        account_mos_test = General("DEA-MOS-Test", **{"fillcolor": colors["account"]})
                        account_mos_pre_prod = General("DEA-MOS-PreProd", **{"fillcolor": colors["account"]})
                        account_mos_staging = General("DEA-MOS-Staging", **{"fillcolor": colors["account"]})

                ou_firebird = General("Firebird", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_firebird_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_firebird_mig_prod = General("DEA-Firebird-Mig-Prod", **{"fillcolor": colors["account"]})
                        account_dea_spider_mig_prod = General("DEA-Spider-Mig-Prod", **{"fillcolor": colors["account"]})
                    ou_firebird_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_firebird_mig_non_prod = General("DEA-Firebird-Mig-NonProd", **{"fillcolor": colors["account"]})
                        account_dea_laas_mig_non_prod = General("DEA-LaaS-Mig-NonProd", **{"fillcolor": colors["account"]})
                        accoubt_dea_chinook_mig_non_prod = General("DEA-Chinook-Mig-NonProd", **{"fillcolor": colors["account"]})

                ou_st = General("ST", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_st_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_st_mig_prod = General("DEA-ST-Mig-Prod", **{"fillcolor": colors["account"]})
                    ou_st_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_st_mig_non_prod = General("DEA-ST-Mig-NonProd", **{"fillcolor": colors["account"]})

                ou_epic = General("EPIC", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_epic_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_epic_mig_prod = General("DEA-EPIC-Mig-Prod", **{"fillcolor": colors["account"]})
                    ou_epic_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

                    with Cluster("Account Level"):
                        account_dea_epic_mig_non_prod = General("DEA-EPIC-Mig-NonProd", **{"fillcolor": colors["account"]})

                ou_diversion = General("Diversion", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_diversion_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_csos_prod = General("DEA-Diversion-Mig-Prod", **{"fillcolor": colors["account"]})
                        account_dea_diversion_management = General("DEA-Diversion-Management", **{"fillcolor": colors["account"]})
                        account_dea_diversion_mig_csos1_prod = General("DEA-Diversion-Mig-CSOS1-Prod", **{"fillcolor": colors["account"]})
                        account_dea_diversion_mig_rsn_prod = General("DEA-Diversion-Mig-RSN-Prod", **{"fillcolor": colors["account"]})
                    ou_diversion_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_csos_non_prod = General("DEA-CSOS-NonProd", **{"fillcolor": colors["account"]})
                        account_dea_mig_staging = General("DEA-Mig-Staging", **{"fillcolor": colors["account"]})
                        account_dea_diversion_csos1_dev = General("DEA-Diversion-CSOS1-Dev", **{"fillcolor": colors["account"]})
                        account_dea_diversion_mig_rsn_test = General("DEA-Diversion-Mig-RSN-Test", **{"fillcolor": colors["account"]})
                        account_rsn_preprod = General("RSN-PreProd", **{"fillcolor": colors["account"]})
                        account_diversion_mig_csos1_staging = General("DEA-Diversion-Mig-CSOS1-Staging", **{"fillcolor": colors["account"]})
                        account_diversion_mig_rsn_dev = General("DEA-Diversion-Mig-RSN-Dev", **{"fillcolor": colors["account"]})

                ou_dso = General("DSO", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_dso_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_dso_app_prod = General("DEA-DSO-App-Prod", **{"fillcolor": colors["account"]})
                    ou_dso_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_dso_app_dev = General("DEA-DSO-App-Dev", **{"fillcolor": colors["account"]})
                        account_dea_dso_app_test = General("DEA-DSO-App-Test", **{"fillcolor": colors["account"]})
                        account_dea_dso_app_pre_prod = General("DEA-DSO-App-PreProd", **{"fillcolor": colors["account"]})

                ou_mso = General("MSO", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_mso_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    ou_mso_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

                ou_sfl1 = General("SFL1", **{"fillcolor": colors["ou_level2"]})
                with Cluster("OU Level 3"):
                    ou_sfl1_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    ou_sfl1_non_prod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})

            ou_ext_tenants = General("EXT-Tenants", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    ou_nonprod = General("Non-Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_app_ext_preprod = General("DEA-APP-EXT-PreProd", **{"fillcolor": colors["account"]})
                        account_dea_dice_ext_dtp = General("DEA-DICE-EXT-DTP", **{"fillcolor": colors["account"]})

                    ou_prod = General("Production", **{"fillcolor": colors["ou_level3"]})
                    with Cluster("Account Level"):
                        account_dea_app_ext_prod = General("DEA-APP-EXT-Prod", **{"fillcolor": colors["account"]})
                        account_dea_dice_ext_prod = General("DEA-DICE-EXT-Prod", **{"fillcolor": colors["account"]})

            ou_policy_staging = General("Policy Staging", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    with Cluster("Account Level"):
                        account_policy_staging = General("Policy Staging", **{"fillcolor": colors["account"]})

            ou_deployments = General("Deployments", **{"fillcolor": colors["ou_level1"]})
            with Cluster("OU Level 2"):
                with Cluster("OU Level 3"):
                    with Cluster("Account Level"):
                        account_dea_dso_preproduction = General("DEA-DSO-PreProduction", **{"fillcolor": colors["account"]})
                        account_dea_dso_production = General("DEA-DSO-Production", **{"fillcolor": colors["account"]})
                        account_dea_dso_test = General("DEA-DSO-Test", **{"fillcolor": colors["account"]})

    # Connect nodes
    root >> ou_sandbox
    root >> ou_security
    root >> ou_infrastructure
    root >> ou_tenants
    root >> ou_ext_tenants
    root >> ou_policy_staging
    root >> ou_deployments

    ou_sandbox >> ou_sandbox_norestrictvpc
    ou_sandbox >> ou_sandbox_restrictvpc
    ou_sandbox_norestrictvpc >> account_dea_tcvv_sandbox

    ou_security >> account_dea_security
    ou_security >> account_log_archive

    ou_infrastructure >> account_dea_stratus_mgn_staging
    ou_infrastructure >> account_network
    ou_infrastructure >> account_shared_services
    ou_infrastructure >> account_dea_workspaces_test
    ou_infrastructure >> account_dea_workspaces

    ou_tenants >> ou_sod
    ou_sod >> ou_sod_prod
    ou_sod >> ou_sod_non_prod
    ou_tenants >> ou_datalakes
    ou_datalakes >> ou_datalakes_prod
    ou_datalakes >> ou_datalakes_non_prod
    ou_tenants >> ou_intel
    ou_tenants >> ou_firebird
    ou_firebird >> ou_firebird_prod
    ou_firebird >> ou_firebird_non_prod
    ou_firebird_non_prod >> account_dea_firebird_mig_non_prod
    ou_firebird_non_prod >> account_dea_laas_mig_non_prod
    ou_firebird_non_prod >> accoubt_dea_chinook_mig_non_prod
    ou_firebird_prod >> account_dea_firebird_mig_prod
    ou_firebird_prod >> account_dea_spider_mig_prod

    ou_tenants >> ou_st
    ou_st >> ou_st_prod
    ou_st >> ou_st_non_prod
    ou_st_non_prod >> account_dea_st_mig_non_prod
    ou_st_prod >> account_dea_st_mig_prod

    ou_tenants >> ou_epic
    ou_epic >> ou_epic_prod
    ou_epic >> ou_epic_non_prod
    ou_epic_non_prod >> account_dea_epic_mig_non_prod
    ou_epic_prod >> account_dea_epic_mig_prod

    ou_tenants >> ou_diversion
    ou_diversion >> ou_diversion_prod
    ou_diversion >> ou_diversion_non_prod
    ou_diversion_non_prod >> account_dea_csos_non_prod
    ou_diversion_non_prod >> account_dea_mig_staging
    ou_diversion_non_prod >> account_dea_diversion_csos1_dev
    ou_diversion_non_prod >> account_dea_diversion_mig_rsn_test
    ou_diversion_non_prod >> account_rsn_preprod
    ou_diversion_non_prod >> account_diversion_mig_csos1_staging
    ou_diversion_non_prod >> account_diversion_mig_rsn_dev
    ou_diversion_prod >> account_dea_csos_prod
    ou_diversion_prod >> account_dea_diversion_management
    ou_diversion_prod >> account_dea_diversion_mig_csos1_prod
    ou_diversion_prod >> account_dea_diversion_mig_rsn_prod

    ou_tenants >> ou_dso
    ou_dso >> ou_dso_prod
    ou_dso >> ou_dso_non_prod
    ou_dso_prod >> account_dea_dso_app_prod
    ou_dso_non_prod >> account_dea_dso_app_dev
    ou_dso_non_prod >> account_dea_dso_app_test
    ou_dso_non_prod >> account_dea_dso_app_pre_prod

    ou_tenants >> ou_mso
    ou_mso >> ou_mso_prod
    ou_mso >> ou_mso_non_prod

    ou_tenants >> ou_sfl1
    ou_sfl1 >> ou_sfl1_prod
    ou_sfl1 >> ou_sfl1_non_prod

    ou_ext_tenants >> ou_nonprod
    ou_ext_tenants >> ou_prod

    ou_nonprod >> account_dea_app_ext_preprod
    ou_nonprod >> account_dea_dice_ext_dtp
    ou_prod >> account_dea_app_ext_prod
    ou_prod >> account_dea_dice_ext_prod

    ou_policy_staging >> account_policy_staging

    ou_deployments >> account_dea_dso_preproduction
    ou_deployments >> account_dea_dso_production
    ou_deployments >> account_dea_dso_test

    ou_intel >> ou_intel_non_prod
    ou_intel >> ou_intel_prod

    ou_intel_prod >> account_dea_concorde_prod
    ou_intel_prod >> account_dea_speedwayu_mig_prod
    ou_intel_prod >> account_dea_ctt_prod
    ou_intel_prod >> account_mos_prod
    ou_intel_non_prod >> account_dea_concorde_pre_prod
    ou_intel_non_prod >> account_dea_speedwayu_mig_non_prod
    ou_intel_non_prod >> account_dea_ctt_non_prod
    ou_intel_non_prod >> account_dea_concorde_test
    ou_intel_non_prod >> account_mos_dev
    ou_intel_non_prod >> account_mos_test
    ou_intel_non_prod >> account_mos_pre_prod
    ou_intel_non_prod >> account_mos_staging
