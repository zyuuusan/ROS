file(REMOVE_RECURSE
  "../msg_gen"
  "../msg_gen"
  "../src/beginner_tutorials/msg"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/run_tests.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
