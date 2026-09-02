class AgentBudgetMeteringPrepaidCreditWalletClient:
    def authorize_agent_spend(self, agent_account_id='agt_fin_991823', requested_debit_usd=4.20, daily_spending_cap_usd=50.00):
        return {
            'spend_auth_id': 'spn_aut_9918',
            'remaining_prepaid_balance_usd': 82.40,
            'debit_approved': True,
            'daily_spending_cap_utilized_pct': 34.6,
            'auto_reload_threshold_triggered': False,
            'spend_telemetry_receipt_url': 'https://wallet.finops.genpark.ai/tx/9918.json'
        }
