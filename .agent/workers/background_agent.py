# Deprecated in ARC Protocol 3.0.
# Background model execution was removed in favor of host-native Skills orchestration.
# This shim intentionally fails with migration guidance instead of launching Gemini.
import sys

if __name__ == "__main__":
    print(
        "ARC v3 no longer launches model-specific background workers. "
        "Use the arc-execute Skill and your host agent's native delegation features. "
        "See docs/MIGRATION_V3.md.",
        file=sys.stderr,
    )
    raise SystemExit(2)
