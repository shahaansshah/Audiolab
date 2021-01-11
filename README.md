# Audiolab
A space for the development of audio-related tools.

## Proposed Development: `signalfinder`
#### The idea
You have an audio file in which you can mark all the points in which a
certain impulse occurs - perhaps a snare drum hit, an adlib '*yuh*',
or a synth melody (in which case maybe you also specify the notes).
With just that information, `signalfinder` is told to find the 'recurring
signal'. What happens?? This is very related to
`soundremover` - in both cases, a certain signal needs to be isolated.

#### Related Steps To That End
- `view_state_space(phase, amplitude, etc.)`
    - a much dumber `soundremover`

---

#### Other Tasks
- Consult whether my project structure & import methods are solid
