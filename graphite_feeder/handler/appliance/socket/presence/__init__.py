import home

from graphite_feeder.handler.appliance.socket.energy_guard import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.socket.presence.Appliance

    def _get_url(self, name):
        url = 'target=alias(offset(keepLastValue({name}.{metric}), 0),"Forced on")&'.format(
            name=name, metric=self.metric
        )
        url += 'target=alias(offset(keepLastValue({name}.{metric}), 1),"Off")&'.format(
            name=name, metric=self.metric
        )
        return url

    def get_datapoint(self):
        if (
            self._appliance.state.VALUE
            == home.appliance.socket.presence.state.off.State().VALUE
        ):
            return 0
        if (
            self._appliance.state.VALUE
            == home.appliance.socket.presence.state.forced.on.State().VALUE
        ):
            return 1


from graphite_feeder.handler.appliance.socket.presence import christmas
