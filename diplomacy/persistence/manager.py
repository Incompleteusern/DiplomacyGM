from diplomacy.adjudicator.adjudicator import Adjudicator
from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector.vector import parse as parse_board
from diplomacy.persistence.board import Board
from diplomacy.persistence.order import Order
from diplomacy.persistence.player import Player


# TODO: (DB) variants table that holds starting state & map: insert parsed Imp Dip for now
# TODO: (DB) games table (copy of a variant data, has server ID)


class Manager:
    """Manager acts as an intermediary between Bot (the Discord API), Board (the board state), the database."""

    def __init__(self):
        self._boards: dict[int, Board] = {}

    def create_game(self, server_id: int) -> str:
        if self._boards[server_id]:
            raise RuntimeError("A game already exists in this server.")

        # TODO: (DB) get board from variant DB
        self._boards[server_id] = parse_board()

        # TODO: (DB) return map state
        raise RuntimeError("Game creation has not yet been implemented.")

    def get_board(self, server_id: int) -> Board:
        board = self._boards[server_id]
        if not board:
            raise RuntimeError("There is no existing game this this server.")
        return board

    def add_orders(self, server_id: int, orders: list[Order]) -> None:
        self._boards[server_id].add_orders(orders)
        # TODO: (DB) overwrite order for unit in DB
        raise RuntimeError("Add orders to database has not yet been implemented.")

    def get_moves_map(self, server_id: int, player_restriction: Player | None) -> str:
        return Mapper(self._boards[server_id]).get_moves_map(player_restriction)

    def adjudicate(self, server_id: int) -> str:
        # TODO: (DB) get retreat map from DB
        board = Adjudicator(self._boards[server_id]).adjudicate()
        self._boards[server_id] = board
        mapper = Mapper(board)
        moves_map = mapper.get_moves_map(None)
        results_map = mapper.get_results_map()
        # TODO: (DB) update board, moves map, results map at server id at turn in db
        # TODO: (DB) protect against malicious inputs (ex. orders) like drop table
        # TODO: (MAP) return both moves and results map
        raise RuntimeError("Adjudication map return not yet implemented.")

    def rollback(self) -> str:
        # TODO: (DB) get former turn board & moves map & results map from DB; update board; return maps
        raise RuntimeError("Rollback not yet implemented.")
