import itertools
from typing import Sequence

from yql.essentials.providers.common.proto.gateways_config_pb2 import EGenericDataSourceKind, EGenericProtocol
from ydb.public.api.protos.ydb_value_pb2 import Type

import ydb.library.yql.providers.generic.connector.tests.utils.types.mongodb as mongodb
from ydb.library.yql.providers.generic.connector.tests.utils.schema import (
    Schema,
    Column,
    ColumnList,
    DataSourceType,
    SelectWhat,
    makeOptionalYdbTypeFromTypeID
)

from ydb.library.yql.providers.generic.connector.tests.common_test_cases.select_positive_common import TestCase


class Factory:
    def _primitive_types(self) -> Sequence[TestCase]:
        """
        Every data source has its own type system;
        we test datasource-specific types in the following test cases.
        """
        schema = Schema(
            columns=ColumnList(
                Column(
                    name='_id',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.STRING),
                    data_source_type=DataSourceType(mng=mongodb.ObjectId()),
                ),
                Column(
                    name='a',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.BOOL),
                    data_source_type=DataSourceType(mng=mongodb.Boolean()),
                ),
                Column(
                    name='b',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.INT32),
                    data_source_type=DataSourceType(mng=mongodb.Int32()),
                ),
                Column(
                    name='c',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.INT64),
                    data_source_type=DataSourceType(mng=mongodb.Int64()),
                ),
                Column(
                    name='d',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.DOUBLE),
                    data_source_type=DataSourceType(mng=mongodb.Double()),
                ),
                Column(
                    name='e',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.UTF8),
                    data_source_type=DataSourceType(mng=mongodb.String()),
                ),
                Column(
                    name='f',
                    ydb_type=makeOptionalYdbTypeFromTypeID(type_id=Type.STRING),
                    data_source_type=DataSourceType(mng=mongodb.Binary()),
                ),
            )
        )

        basic = TestCase(
            name_='primitives',
            schema=schema,
            select_what=SelectWhat.asterisk(schema.columns),
            select_where=None,
            data_in=None,
            data_out_=[
                [
                    bytes.fromhex('171e75500ecde1c75c59139e'),
                    True,
                    42,
                    23423,
                    1.22,
                    "hello",
                    b'\xaa\xaa',
                ],
                [
                    bytes.fromhex('271e75500ecde1c75c59139e'),
                    False,
                    13,
                    13,
                    1.23,
                    "hi",
                    b'\xab\xab',
                ],
                [
                    bytes.fromhex('371e75500ecde1c75c59139e'),
                    False,
                    15,
                    15,
                    1.24,
                    "bye",
                    b'\xac\xac',
                ]
            ],
            data_source_kind=EGenericDataSourceKind.MONGO_DB,
            protocol=EGenericProtocol.NATIVE,
            pragmas=dict(),
            check_output_schema=True,
        )

        missing = TestCase(
            name_='missing',
            schema=schema,
            select_what=SelectWhat.asterisk(schema.columns),
            select_where=None,
            data_in=None,
            data_out_=[
                [
                    bytes.fromhex('171e75500ecde1c75c59139e'),
                    None,
                    32,
                    23423,
                    1.1,
                    "hello",
                    None
                ],
                [
                    bytes.fromhex('271e75500ecde1c75c59139e'),
                    True,
                    64,
                    None,
                    1.2,
                    None,
                    b'\xab\xcd',
                ],
                [
                    bytes.fromhex('371e75500ecde1c75c59139e'),
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                ]
            ],
            data_source_kind=EGenericDataSourceKind.MONGO_DB,
            protocol=EGenericProtocol.NATIVE,
            pragmas=dict(),
            check_output_schema=True,
        )

        return [basic, missing]

    def _constant(self) -> Sequence[TestCase]:
        '''
        In this test case set we check SELECT 42 from a MongoDB collection.
        '''

        schema = Schema(
            columns=ColumnList(
                Column(
                    name='_id',
                    ydb_type=Type.INT32,
                    data_source_type=DataSourceType(mng=mongodb.Int32()),
                ),
            )
        )

        test_case_name = 'constant'

        tc = TestCase(
            name_=test_case_name,
            schema=schema,
            select_what=SelectWhat(SelectWhat.Item(name='42', kind='expr')),
            select_where=None,
            data_in=None,
            data_out_=[
                [
                    42,
                ],
                [
                    42,
                ],
                [
                    42,
                ],
            ],
            data_source_kind=EGenericDataSourceKind.MONGO_DB,
            protocol=EGenericProtocol.NATIVE,
            pragmas=dict(),
        )

        return [tc]

    def _count_rows(self) -> Sequence[TestCase]:
        '''
        In this test case set we check SELECT COUNT(*) from a MongoDB collection.
        '''

        schema = Schema(
            columns=ColumnList(
                Column(
                    name='_id',
                    ydb_type=Type.INT32,
                    data_source_type=DataSourceType(mng=mongodb.Int32()),
                ),
            )
        )

        test_case_name = 'count_rows'

        tc = TestCase(
            name_=test_case_name,
            schema=schema,
            select_what=SelectWhat(SelectWhat.Item(name='COUNT(*)', kind='expr')),
            select_where=None,
            data_in=None,
            data_out_=[
                [
                    3,
                ],
            ],
            data_source_kind=EGenericDataSourceKind.MONGO_DB,
            protocol=EGenericProtocol.NATIVE,
            pragmas=dict(),
        )

        return [tc]

    def make_test_cases(self) -> Sequence[TestCase]:
        return list(
            itertools.chain(
                self._primitive_types(),
                self._constant(),
                self._count_rows(),
            )
        )
