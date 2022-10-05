#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# Copyright (c) 2022, QuatroPe
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""test for skcriteria.core.plots

"""


# =============================================================================
# IMPORTS
# =============================================================================

from unittest import mock

from matplotlib import pyplot as plt
from matplotlib.testing.decorators import check_figures_equal

import pytest

import seaborn as sns

from skcriteria.core import plot


# =============================================================================
# HEATMAP
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_heatmap(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.heatmap(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.heatmap(df, ax=exp_ax, annot=True, cmap=plt.cm.get_cmap())


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wheatmap(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wheatmap(ax=test_ax)

    # EXPECTED
    df = dm.weights.to_frame().T
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.heatmap(df, ax=exp_ax, annot=True, cmap=plt.cm.get_cmap())


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wheatmap_default_axis(
    decision_matrix, fig_test, fig_ref
):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    with mock.patch("matplotlib.pyplot.gca", return_value=test_ax):
        plotter.wheatmap()

    # EXPECTED
    labels = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]

    weights = dm.weights.to_frame().T

    exp_ax = fig_ref.subplots()
    sns.heatmap(weights, ax=exp_ax, annot=True, cmap=plt.cm.get_cmap())

    exp_ax.set_xticklabels(labels)
    exp_ax.set_xlabel("Criteria")

    size = fig_ref.get_size_inches() / [1, 5]
    fig_ref.set_size_inches(size)


# =============================================================================
# BAR
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_bar(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.bar(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    df.plot.bar(ax=exp_ax)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wbar(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wbar(ax=test_ax)

    # EXPECTED
    df = dm.weights.to_frame().T
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    df.plot.bar(ax=exp_ax)


# =============================================================================
# BARH
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_barh(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.barh(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    df.plot.barh(ax=exp_ax)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wbarh(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wbarh(ax=test_ax)

    # EXPECTED
    df = dm.weights.to_frame().T
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    df.plot.barh(ax=exp_ax)


# =============================================================================
# HIST
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_hist(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.hist(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.histplot(data=df, ax=exp_ax)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_whist(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.whist(ax=test_ax)

    # EXPECTED
    df = dm.weights.to_frame().T
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.histplot(data=df, ax=exp_ax)


# =============================================================================
# BOX
# =============================================================================


@pytest.mark.slow
@pytest.mark.parametrize("orient", ["v", "h"])
@check_figures_equal()
def test_DecisionMatrixPlotter_box(decision_matrix, orient, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.box(ax=test_ax, orient=orient)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.boxplot(data=df, ax=exp_ax, orient=orient)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wbox(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wbox(ax=test_ax)

    # EXPECTED
    weights = dm.weights.to_frame()

    exp_ax = fig_ref.subplots()
    sns.boxplot(data=weights, ax=exp_ax)


# =============================================================================
# KDE
# =============================================================================
@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_kde(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.kde(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.kdeplot(data=df, ax=exp_ax)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wkde(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wkde(ax=test_ax)

    # EXPECTED
    weights = dm.weights.to_frame()

    exp_ax = fig_ref.subplots()
    sns.kdeplot(data=weights, ax=exp_ax)


# =============================================================================
# OGIVE
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_ogive(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.ogive(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    sns.ecdfplot(data=df, ax=exp_ax)


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_wogive(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.wogive(ax=test_ax)

    # EXPECTED
    weights = dm.weights.to_frame()

    exp_ax = fig_ref.subplots()
    sns.ecdfplot(data=weights, ax=exp_ax)


# =============================================================================
# AREA
# =============================================================================


@pytest.mark.slow
@check_figures_equal()
def test_DecisionMatrixPlotter_area(decision_matrix, fig_test, fig_ref):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.area(ax=test_ax)

    # EXPECTED
    df = dm.matrix
    df.columns = [
        f"{c} {o.to_symbol()}" for c, o in zip(dm.criteria, dm.objectives)
    ]
    df.columns.name = "Criteria"

    exp_ax = fig_ref.subplots()
    df.plot.area(ax=exp_ax)


# =============================================================================
# DOMINANCE
# =============================================================================


@pytest.mark.slow
@pytest.mark.parametrize("strict", [True, False])
@check_figures_equal()
def test_DecisionMatrixPlotter_dominance(
    decision_matrix, fig_test, fig_ref, strict
):
    dm = decision_matrix(
        seed=42,
        min_alternatives=3,
        max_alternatives=3,
        min_criteria=3,
        max_criteria=3,
    )

    plotter = plot.DecisionMatrixPlotter(dm=dm)

    test_ax = fig_test.subplots()
    plotter.dominance(strict=strict, ax=test_ax)

    # EXPECTED

    exp_ax = fig_ref.subplots()
    sns.heatmap(
        dm.dominance.dominance(strict=strict),
        ax=exp_ax,
        annot=False,
        cmap=plt.cm.get_cmap(),
        cbar=False,
    )
