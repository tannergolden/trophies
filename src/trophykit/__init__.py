# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Trophy Kit: trophies a GitHub profile or repository earns for itself.

Stdlib-only. A scheduled action measures the subject over GitHub's API,
this package draws the result as committed SVGs, and nothing is fetched
when a README is viewed.
"""

# Bumped whenever rendered output changes for the same input. Every SVG is
# stamped with it; --check hard-fails only same-version drift and treats a
# version difference as "regenerate on the next run", so a kit release can
# never wedge a consumer's schedule.
KIT_VERSION = "2"
