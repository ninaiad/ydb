import pytest

from yql.essentials.providers.common.proto.gateways_config_pb2 import EGenericDataSourceKind
from ydb.library.yql.providers.generic.connector.tests.utils.settings import Settings
from ydb.library.yql.providers.generic.connector.tests.utils.run.runners import runner_types, configure_runner

from conftest import docker_compose_dir
from collection import Collection

import ydb.library.yql.providers.generic.connector.tests.utils.scenario.mongodb as scenario
import ydb.library.yql.providers.generic.connector.tests.common_test_cases.select_positive_common as select_positive_common


# Global collection of test cases dependent on environment
tc_collection = Collection(
    Settings.from_env(docker_compose_dir=docker_compose_dir, data_source_kinds=[EGenericDataSourceKind.MONGO_DB])
)


@pytest.mark.parametrize("runner_type", runner_types)
@pytest.mark.parametrize("test_case", tc_collection.get('select_positive'), ids=tc_collection.ids('select_positive'))
@pytest.mark.usefixtures("settings")
def test_select_positive(
    request: pytest.FixtureRequest,
    settings: Settings,
    runner_type: str,
    test_case: select_positive_common.TestCase,
):
    runner = configure_runner(runner_type=runner_type, settings=settings)
    scenario.select_positive(
        settings=settings,
        runner=runner,
        test_case=test_case,
        test_name=request.node.name,
    )
