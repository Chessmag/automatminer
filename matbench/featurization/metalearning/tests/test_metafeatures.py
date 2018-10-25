import unittest
from matbench.featurization.metalearning.metafeatures import *
from matbench.data.load import load_castelli_perovskites, load_glass_binary


class TestFormulaMetafeatures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df_glass = load_glass_binary()

    def test_NumberOfFormulas(self):
        nf = NumberOfFormulas().calc(self.df_glass["formula"])
        self.assertEqual(nf, 5959)

    def test_PercentOfAllMetal(self):
        pm = PercentOfAllMetal().calc(self.df_glass["formula"])
        self.assertAlmostEqual(pm, 0.6578, 4)

    def test_PercentOfMetalNonmetal(self):
        pmnc = PercentOfMetalNonmetal().calc(self.df_glass["formula"])
        self.assertAlmostEqual(pmnc, 0.3208, 4)

    def test_PercentOfAllNonmetal(self):
        pan = PercentOfAllNonmetal().calc(self.df_glass["formula"])
        self.assertAlmostEqual(pan, 0.0214, 4)

    def test_PercentOfContainTransMetal(self):
        pctm = PercentOfContainTransMetal().calc(self.df_glass["formula"])
        self.assertAlmostEqual(pctm, 0.6877, 4)

    def test_NumberOfDifferentElements(self):
        nde = NumberOfDifferentElements().calc(self.df_glass["formula"])
        self.assertEqual(nde, 38)

    def test_AvgNumberOfElements(self):
        ane = AvgNumberOfElements().calc(self.df_glass["formula"])
        self.assertAlmostEqual(ane, 1.9802, 4)

    def test_MaxNumberOfElements(self):
        mne = MaxNumberOfElements().calc(self.df_glass["formula"])
        self.assertEqual(mne, 2)

    def test_MinNumberOfElements(self):
        mne = MinNumberOfElements().calc(self.df_glass["formula"])
        self.assertEqual(mne, 1)


class TestStructureMetafeatures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df_castelli = load_castelli_perovskites()
        cls.df_castelli["structure"] = cls.df_castelli["structure"].\
            apply(lambda x: Structure.from_dict(x))

    def test_NumberOfStructures(self):
        ns = NumberOfStructures().calc(self.df_castelli["structure"])
        self.assertEqual(ns, 18928)

    def test_PercentOfOrderedStructures(self):
        pos = PercentOfOrderedStructures().calc(self.df_castelli["structure"])
        self.assertAlmostEqual(pos, 1.0)

    def test_AvgNumberOfSitess(self):
        ans = AvgNumberOfSites().calc(self.df_castelli["structure"])
        self.assertAlmostEqual(ans, 5.0)

    def test_MaxNumberOfSites(self):
        mns = MaxNumberOfSites().calc(self.df_castelli["structure"])
        self.assertAlmostEqual(mns, 5.0)

    def test_NumberOfDifferentElementsInStructure(self):
        mns = NumberOfDifferentElementsInStructure().calc(
            self.df_castelli["structure"])
        self.assertEqual(mns, 56)


if __name__ == "__main__":
    unittest.main()