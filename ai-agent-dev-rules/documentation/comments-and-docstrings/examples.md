# Comments and Docstrings Examples

**Rule ID:** `DOC-COMMENTS-EXAMPLES`  
**Status:** Active.  
**Applies when:** The required documentation format is unclear, a new pattern is being introduced, or the repository has no nearby valid example.  
**Required pages:** `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.1.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Python function

```python
def load_profile(profile_name: str) -> Profile:
    """Loads one validated profile by its stable name.

    Args:
        profile_name: Stable profile name without a file extension.

    Returns:
        The parsed and validated profile.

    Raises:
        ProfileNotFoundError: The named profile does not exist.
        ProfileValidationError: The profile content is invalid.
    """
```

## TypeScript component

```ts
/**
 * Renders the application bar and owns its navigation entry points.
 *
 * @param props - Application bar configuration.
 * @param props.hideBurger - Hides the desktop navigation trigger.
 * @returns The application header and connected drawer markup.
 */
export function AppBar({ hideBurger = false }: AppBarProps) {
  // Implementation.
}
```

## Concise internal helper

```ts
/** Returns whether the supplied route belongs to the administration area. */
function isAdministrationRoute(path: string): boolean {
  return path.startsWith("/admin/");
}
```

## Logical groups

```ts
const navigate = useNavigate();

// Colors.
const neutral = neutralColors;
const danger = dangerColors;

//
// Menu state.
// The profile menu and drawer use independent state because desktop and
// mobile navigation can be opened through different interaction paths.
//
const [showProfileMenu, setShowProfileMenu] = useState(false);
const [drawerOpen, setDrawerOpen] = useState(false);
```

## Bash function

```bash
#
# Resolves the configured installation root.
#
# Args:
#   $1: Optional installation root override.
#
# Outputs:
#   The absolute installation root.
#
# Returns:
#   0 when the path is valid.
#
resolve_install_root() {
  local override="${1:-}"
}
```

## PowerShell function

```powershell
<#
.SYNOPSIS
Resolves the configured application root.

.PARAMETER Root
Optional application root override.

.OUTPUTS
System.String. The normalized absolute path.
#>
function Resolve-ApplicationRoot {
    param(
        [string]$Root
    )
}
```

## File-level documentation

```python
"""Coordinates authenticated API route registration.

The module owns route composition only. Authentication verification remains
in the auth service, while persistence remains in repository classes.
"""
```

Do not copy an example mechanically when the language or repository already defines a more specific valid convention.
