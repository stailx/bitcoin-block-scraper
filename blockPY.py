# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Input:
    sequence: int
    witness: str
    script: str
    index: int
    prev_out: None

    def __init__(self, sequence: int, witness: str, script: str, index: int, prev_out: None) -> None:
        self.sequence = sequence
        self.witness = witness
        self.script = script
        self.index = index
        self.prev_out = prev_out

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        assert isinstance(obj, dict)
        sequence = from_int(obj.get("sequence"))
        witness = from_str(obj.get("witness"))
        script = from_str(obj.get("script"))
        index = from_int(obj.get("index"))
        prev_out = from_none(obj.get("prev_out"))
        return Input(sequence, witness, script, index, prev_out)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sequence"] = from_int(self.sequence)
        result["witness"] = from_str(self.witness)
        result["script"] = from_str(self.script)
        result["index"] = from_int(self.index)
        result["prev_out"] = from_none(self.prev_out)
        return result


class Out:
    type: int
    spent: bool
    value: int
    spending_outpoints: List[Any]
    n: int
    tx_index: int
    script: str
    addr: str

    def __init__(self, type: int, spent: bool, value: int, spending_outpoints: List[Any], n: int, tx_index: int, script: str, addr: str) -> None:
        self.type = type
        self.spent = spent
        self.value = value
        self.spending_outpoints = spending_outpoints
        self.n = n
        self.tx_index = tx_index
        self.script = script
        self.addr = addr

    @staticmethod
    def from_dict(obj: Any) -> 'Out':
        assert isinstance(obj, dict)
        type = from_int(obj.get("type"))
        spent = from_bool(obj.get("spent"))
        value = from_int(obj.get("value"))
        spending_outpoints = from_list(lambda x: x, obj.get("spending_outpoints"))
        n = from_int(obj.get("n"))
        tx_index = from_int(obj.get("tx_index"))
        script = from_str(obj.get("script"))
        addr = from_str(obj.get("addr"))
        return Out(type, spent, value, spending_outpoints, n, tx_index, script, addr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_int(self.type)
        result["spent"] = from_bool(self.spent)
        result["value"] = from_int(self.value)
        result["spending_outpoints"] = from_list(lambda x: x, self.spending_outpoints)
        result["n"] = from_int(self.n)
        result["tx_index"] = from_int(self.tx_index)
        result["script"] = from_str(self.script)
        result["addr"] = from_str(self.addr)
        return result


class Tx:
    hash: str
    ver: int
    vin_sz: int
    vout_sz: int
    size: int
    weight: int
    fee: int
    relayed_by: str
    lock_time: int
    tx_index: int
    double_spend: bool
    time: int
    block_index: int
    block_height: int
    inputs: List[Input]
    out: List[Out]
    hex: str

    def __init__(self, hash: str, ver: int, vin_sz: int, vout_sz: int, size: int, weight: int, fee: int, relayed_by: str, lock_time: int, tx_index: int, double_spend: bool, time: int, block_index: int, block_height: int, inputs: List[Input], out: List[Out], hex: str) -> None:
        self.hash = hash
        self.ver = ver
        self.vin_sz = vin_sz
        self.vout_sz = vout_sz
        self.size = size
        self.weight = weight
        self.fee = fee
        self.relayed_by = relayed_by
        self.lock_time = lock_time
        self.tx_index = tx_index
        self.double_spend = double_spend
        self.time = time
        self.block_index = block_index
        self.block_height = block_height
        self.inputs = inputs
        self.out = out
        self.hex = hex

    @staticmethod
    def from_dict(obj: Any) -> 'Tx':
        assert isinstance(obj, dict)
        hash = from_str(obj.get("hash"))
        ver = from_int(obj.get("ver"))
        vin_sz = from_int(obj.get("vin_sz"))
        vout_sz = from_int(obj.get("vout_sz"))
        size = from_int(obj.get("size"))
        weight = from_int(obj.get("weight"))
        fee = from_int(obj.get("fee"))
        relayed_by = from_str(obj.get("relayed_by"))
        lock_time = from_int(obj.get("lock_time"))
        tx_index = from_int(obj.get("tx_index"))
        double_spend = from_bool(obj.get("double_spend"))
        time = from_int(obj.get("time"))
        block_index = from_int(obj.get("block_index"))
        block_height = from_int(obj.get("block_height"))
        inputs = from_list(Input.from_dict, obj.get("inputs"))
        out = from_list(Out.from_dict, obj.get("out"))
        hex = from_str(obj.get("hex"))
        return Tx(hash, ver, vin_sz, vout_sz, size, weight, fee, relayed_by, lock_time, tx_index, double_spend, time, block_index, block_height, inputs, out, hex)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hash"] = from_str(self.hash)
        result["ver"] = from_int(self.ver)
        result["vin_sz"] = from_int(self.vin_sz)
        result["vout_sz"] = from_int(self.vout_sz)
        result["size"] = from_int(self.size)
        result["weight"] = from_int(self.weight)
        result["fee"] = from_int(self.fee)
        result["relayed_by"] = from_str(self.relayed_by)
        result["lock_time"] = from_int(self.lock_time)
        result["tx_index"] = from_int(self.tx_index)
        result["double_spend"] = from_bool(self.double_spend)
        result["time"] = from_int(self.time)
        result["block_index"] = from_int(self.block_index)
        result["block_height"] = from_int(self.block_height)
        result["inputs"] = from_list(lambda x: to_class(Input, x), self.inputs)
        result["out"] = from_list(lambda x: to_class(Out, x), self.out)
        result["hex"] = from_str(self.hex)
        return result


class Welcome:
    hash: str
    ver: int
    prev_block: str
    mrkl_root: str
    time: int
    bits: int
    next_block: List[str]
    fee: int
    nonce: int
    n_tx: int
    size: int
    block_index: int
    main_chain: bool
    height: int
    weight: int
    tx: List[Tx]

    def __init__(self, hash: str, ver: int, prev_block: str, mrkl_root: str, time: int, bits: int, next_block: List[str], fee: int, nonce: int, n_tx: int, size: int, block_index: int, main_chain: bool, height: int, weight: int, tx: List[Tx]) -> None:
        self.hash = hash
        self.ver = ver
        self.prev_block = prev_block
        self.mrkl_root = mrkl_root
        self.time = time
        self.bits = bits
        self.next_block = next_block
        self.fee = fee
        self.nonce = nonce
        self.n_tx = n_tx
        self.size = size
        self.block_index = block_index
        self.main_chain = main_chain
        self.height = height
        self.weight = weight
        self.tx = tx

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        hash = from_str(obj.get("hash"))
        ver = from_int(obj.get("ver"))
        prev_block = from_str(obj.get("prev_block"))
        mrkl_root = from_str(obj.get("mrkl_root"))
        time = from_int(obj.get("time"))
        bits = from_int(obj.get("bits"))
        next_block = from_list(from_str, obj.get("next_block"))
        fee = from_int(obj.get("fee"))
        nonce = from_int(obj.get("nonce"))
        n_tx = from_int(obj.get("n_tx"))
        size = from_int(obj.get("size"))
        block_index = from_int(obj.get("block_index"))
        main_chain = from_bool(obj.get("main_chain"))
        height = from_int(obj.get("height"))
        weight = from_int(obj.get("weight"))
        tx = from_list(Tx.from_dict, obj.get("tx"))
        return Welcome(hash, ver, prev_block, mrkl_root, time, bits, next_block, fee, nonce, n_tx, size, block_index, main_chain, height, weight, tx)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hash"] = from_str(self.hash)
        result["ver"] = from_int(self.ver)
        result["prev_block"] = from_str(self.prev_block)
        result["mrkl_root"] = from_str(self.mrkl_root)
        result["time"] = from_int(self.time)
        result["bits"] = from_int(self.bits)
        result["next_block"] = from_list(from_str, self.next_block)
        result["fee"] = from_int(self.fee)
        result["nonce"] = from_int(self.nonce)
        result["n_tx"] = from_int(self.n_tx)
        result["size"] = from_int(self.size)
        result["block_index"] = from_int(self.block_index)
        result["main_chain"] = from_bool(self.main_chain)
        result["height"] = from_int(self.height)
        result["weight"] = from_int(self.weight)
        result["tx"] = from_list(lambda x: to_class(Tx, x), self.tx)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
