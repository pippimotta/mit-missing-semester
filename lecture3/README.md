## Exercise3 - Editors(Vim)

Exercises for [lecture3](https://missing.csail.mit.edu/2020/editors/)

1. Complete `vimtutor`. Note: it looks best in a 80x24 (80 columns by 24 lines) terminal window.

2. Download our [basic vimrc](https://missing.csail.mit.edu/2020/files/vimrc) and save it to `~/.vimrc`. Read through the well-commented file (using Vim!), and observe how Vim looks and behaves slightly differently with the new config.

3. Install and config the plugin [ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim)
   1. create the plugins directory with `mkdir -p ~/.vim/pack/vendor/start`
   2. Download the plugin: `cd ~/.vim/pack/vendor/start; git clone https://github.com/ctrlpvim/ctrlp.vim`
   3. Read the [documentation](https://github.com/ctrlpvim/ctrlp.vim/blob/master/readme.md) for the plugin. Try using CtrlP to locate a file by navigating to a project directory, opening Vim, and using the Vim command-line to start `:CtrlP`.
   4. Customize CtrlP by adding [configuration](https://github.com/ctrlpvim/ctrlp.vim/blob/master/readme.md#basic-options) to your `~/.vimrc` to open CtrlP by pressing Ctrl-P
      ```
      let g:ctrlp_map = '<c-p>'
      let g:ctrlp_cmd = 'CtrlP'
      ```
4. Redo the demo on your own machine

5. (Advanced) Convert XML to JSON ([example file](https://missing.csail.mit.edu/2020/files/example-data.xml)) using Vim macros. Try to do this on your own, but you can look at the macros section above if you get stuck.

## Take out

1. using visual mode to copy and paste

   1. enter visual mode
   2. use **motion keys** to select the lines/words
   3. use `y` to do copy

2. using change mode to make modifications quickly
   1. `ci` to modify the content inside quotes
   2. `ci(` and `ci[` to modify the content inside brackets
