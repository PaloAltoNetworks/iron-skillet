# Migrating from legacy skillets to the next-gen model

Prior versions of IronSkillet used the legacy skillet model with the .
meta-cnc.yaml file plus external xml element files. The yaml file snippets
included both the xpath and external snippet file name.

The newer model embeds the xml elements inside the yaml file as a single file
package. Functionally everything else is the same.

The latest skillet model also adds the use of playlists and 'include' 
statements
to reference skillets 
and snippets by name to mix and match configuration elements. As this model
matures, the classic hardcoded method used in this snippet directory will be
deprecated.