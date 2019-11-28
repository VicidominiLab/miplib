import SimpleITK as sitk


def make_translation_transforms_from_xy(xs, ys):
    assert len(xs) == len(ys)
    transforms = []

    for x, y in zip(xs, ys):
        tfm = sitk.TranslationTransform(2)
        tfm.SetParameters((x, y))

        transforms.append(tfm)

    return transforms
