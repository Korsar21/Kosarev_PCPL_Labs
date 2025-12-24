import unittest
from database import (Column, Table, TablesToColumns,
                      get_sorted_columns_by_table,
                      get_table_column_counts,
                      get_columns_ending_with_ov_by_table)

class TestDatabaseQueries(unittest.TestCase):
    def setUp(self):
        self.tables = [
            Table(1, "Основная"),
            Table(2, "Вспомогательная"),
            Table(3, "Архивная")
        ]
        self.columns = [
            Column(101, 1, "Иванов", "Текст"),
            Column(102, 1, "Петров", "Целое"),
            Column(103, 2, "Сидоров", "Дата"),
            Column(104, 3, "Кузнецов", "Текст"),
            Column(105, 3, "Орлов", "Логический")
        ]
        self.tables_to_columns = [
            TablesToColumns(1, 101),
            TablesToColumns(1, 102),
            TablesToColumns(2, 103),
            TablesToColumns(3, 104),
            TablesToColumns(3, 105),
            TablesToColumns(1, 104),
        ]

    def test_get_sorted_columns_by_table(self):
        result = get_sorted_columns_by_table(self.tables, self.columns)
        expected_first_column_id = 101
        expected_last_column_id = 105
        self.assertEqual(result[0][2], expected_first_column_id)
        self.assertEqual(result[-1][2], expected_last_column_id)
        for tbl_id, _, col_id, _ in result:
            col = next(c for c in self.columns if c.id == col_id)
            self.assertEqual(col.id_table, tbl_id)

    def test_get_table_column_counts(self):
        result = get_table_column_counts(self.tables, self.columns)
        expected_order = [(2, 1), (1, 2), (3, 2)]
        for (expected_id, expected_count), (actual_id, actual_count) in zip(expected_order, result):
            self.assertEqual(expected_id, actual_id)
            self.assertEqual(expected_count, actual_count)

    def test_get_columns_ending_with_ov_by_table(self):
        result = get_columns_ending_with_ov_by_table(self.tables, self.columns,
                                                     self.tables_to_columns)
        expected_keys = {"Основная", "Архивная"}
        self.assertSetEqual(set(result.keys()), expected_keys)
        self.assertIn("Кузнецов", result["Основная"])
        self.assertIn("Кузнецов", result["Архивная"])
        self.assertIn("Орлов", result["Архивная"])

if __name__ == '__main__':
    unittest.main(verbosity=2)