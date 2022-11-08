# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from insights.insights.doctype.insights_query.insights_query import InsightsQuery
from insights.insights.doctype.insights_table_import.insights_table_import import (
    InsightsTableImport,
)


class BaseDatabase:
    data_source = None
    connection = None
    query_builder = None
    table_factory = None

    def test_connection(self):
        raise NotImplementedError

    def build_query(self, query: InsightsQuery):
        raise NotImplementedError

    def run_query(self, query: InsightsQuery):
        return self.execute_query(self.build_query(query))

    def execute_query(self, query: str):
        """
        Handles the execution of the query, while also handling closing the connection
        """
        raise NotImplementedError

    def table_exists(self, table: str):
        """
        While importing a table, check if the table exists in the database
        """
        raise NotImplementedError

    def import_table(self, import_doc: InsightsTableImport):
        """
        Imports the table into the database
        """
        raise NotImplementedError

    def sync_tables(self):
        raise NotImplementedError

    def get_table_columns(self, table):
        raise NotImplementedError

    def get_column_options(self, table, column, search_text=None, limit=25):
        raise NotImplementedError

    def get_table_preview(self):
        raise NotImplementedError