hashmal_entry_points = {
    'hashmal.plugin': [
        'Address Encoder = hashmal_lib.plugins.addr_encoder:make_plugin',
        'Block Analyzer = hashmal_lib.plugins.block_analyzer:make_plugin',
        'Blockchain = hashmal_lib.plugins.blockchain:make_plugin',
        'Chainparams = hashmal_lib.plugins.chainparams:make_plugin',
        'Item Types = hashmal_lib.plugins.item_types:make_plugin',
        'Log = hashmal_lib.plugins.log:make_plugin',
        'Script Generator = hashmal_lib.plugins.script_gen:make_plugin',
        'Stack Evaluator = hashmal_lib.plugins.stack:make_plugin',
        'Transaction Analyzer = hashmal_lib.plugins.tx_analyzer:make_plugin',
        'Transaction Builder = hashmal_lib.plugins.tx_builder:make_plugin',
        'Variables = hashmal_lib.plugins.variables:make_plugin',
        'Wallet RPC = hashmal_lib.plugins.wallet_rpc:make_plugin'
    ]
}
