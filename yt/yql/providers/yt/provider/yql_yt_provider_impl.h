#pragma once

#include "yql_yt_provider.h"

#include <yql/essentials/providers/common/transform/yql_visit.h>
#include <yql/essentials/providers/common/transform/yql_exec.h>
#include <yql/essentials/core/yql_graph_transformer.h>
#include <yql/essentials/ast/yql_expr.h>
#include <yql/essentials/core/expr_nodes_gen/yql_expr_nodes_gen.h>
#include <yt/yql/providers/yt/expr_nodes/yql_yt_expr_nodes.h>

#include <util/generic/ptr.h>

namespace NYql {

THolder<IGraphTransformer> CreateYtIODiscoveryTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtEpochTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtIntentDeterminationTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtLoadTableMetadataTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtLoadColumnarStatsTransformer(TYtState::TPtr state);

THolder<TVisitorTransformerBase> CreateYtDataSourceTypeAnnotationTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtDataSourceConstraintTransformer(TYtState::TPtr state);
THolder<TExecTransformerBase> CreateYtDataSourceExecTransformer(TYtState::TPtr state);

THolder<TVisitorTransformerBase> CreateYtDataSinkTypeAnnotationTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtDataSinkConstraintTransformer(TYtState::TPtr state, bool subGraph);
THolder<TExecTransformerBase> CreateYtDataSinkExecTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtDataSinkTrackableNodesCleanupTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtDataSinkFinalizingTransformer(TYtState::TPtr state);

THolder<IGraphTransformer> CreateYtLogicalOptProposalTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtPhysicalOptProposalTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtPhysicalFinalizingTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtPeepholeTransformer(TYtState::TPtr state, const THashMap<TString, TString>& settings);
THolder<IGraphTransformer> CreateYtWideFlowTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtDqHybridTransformer(TYtState::TPtr state, THolder<IGraphTransformer>&& finalizer);
THolder<IGraphTransformer> CreateYtBlockIOFilterTransformer(TYtState::TPtr state, THolder<IGraphTransformer>&& finalizer);
THolder<IGraphTransformer> CreateYtBlockInputTransformer(TYtState::TPtr state);
THolder<IGraphTransformer> CreateYtBlockOutputTransformer(TYtState::TPtr state);

void ScanPlanDependencies(const TExprNode::TPtr& input, TExprNode::TListType& children);
TString MakeTableDisplayName(NNodes::TExprBase table, bool isOutput);

void ScanForUsedOutputTables(const TExprNode& input, TVector<TString>& usedNodeIds);
TString MakeUsedNodeId(const TString& cluster, const TString& table);

} // NYql
