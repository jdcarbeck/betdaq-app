from betdaqAPI import enums

def place_order(selection_id, stake, price, polarity,expected_selection_reset_count,
        expected_withdrawal_sequence_number,cancel_on_in_running=True,cancel_if_selection_reset=True,expires_at=None,
        withdrawal_reprice_option=enums.WithdrawRepriceOption.Cancel.value,
        kill_type=enums.OrderKillType.FillOrKillDontCancel.value, fill_or_kill_threshold=0.0,
        punter_reference_number=1):
        
    resp = {
        '_SelectionId': selection_id,
        '_Stake': stake,
        '_Price': price,
        '_Polarity': polarity,
        '_ExpectedSelectionResetCount': expected_selection_reset_count,
        '_ExpectedWithdrawalSequenceNumber': expected_withdrawal_sequence_number,
        '_CancelOnInRunning': cancel_on_in_running,
        '_CancelIfSelectionReset': cancel_if_selection_reset,
        '_WithdrawalRepriceOption': withdrawal_reprice_option,
        '_KillType': kill_type,
        '_FillOrKillThreshold': fill_or_kill_threshold,
        '_PunterReferenceNumber': punter_reference_number
    }

    if expires_at is not None:
        resp['_ExpiresAt'] = expires_at

    return resp
