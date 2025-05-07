
# #1. Clear Naming

#  calculate_score(player_stats)

# 2. Constants
# Instead of this:

# if attempts > 3:
# Write this:


# MAX_RETRIES = 3
# if attempts > MAX_RETRIES:

# 3. Boolean Function Names

# ✅ is_active(user)

# 4. Avoid Overloading Meaning

# ✅ user_profile, weather_response, monthly_sales_data

# 5. Avoid Nesting
# Before:

# if user:
#     if user.is_authenticated:
#         if user.has_permission:
#             perform_action()
# After:

# if not can_perform_action(user):
#     return
# perform_action()

# 6. Write Small Functions
# ✅ Each one ≤10 lines.
# ✅ Each one doing ONE thing.

# 7. Module-Level Docstring
# At the very top:

# python
# Copy
# Edit
# """Handles user scoring and leaderboard logic."""

# 8. Use Inline Comments Sparingly
# ❌ # loop through items
# ✅ # Skip inactive users to avoid reprocessing
