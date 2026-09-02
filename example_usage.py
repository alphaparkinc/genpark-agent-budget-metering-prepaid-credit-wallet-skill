from client import AgentBudgetMeteringPrepaidCreditWalletClient

def main():
    client = AgentBudgetMeteringPrepaidCreditWalletClient()
    res = client.authorize_agent_spend('agt_search_8812', 12.50, 100.00)
    print('Agent Budget Metering Wallet: ' + res['spend_auth_id'] + ' (Approved: ' + str(res['debit_approved']) + ')')
    print('Remaining Balance: $' + str(res['remaining_prepaid_balance_usd']) + ' | Cap Utilized: ' + str(res['daily_spending_cap_utilized_pct']) + '%')
    print('Receipt URL: ' + res['spend_telemetry_receipt_url'])

if __name__ == '__main__':
    main()
