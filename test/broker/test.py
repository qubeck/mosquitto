#!/usr/bin/env python3

import mosq_test_helper
import ptest

tests = [
    #(ports required, 'path'),
    (1, './01-connect-bad-packet.py'),
    (1, './01-connect-duplicate.py'),
    (1, './01-connect-duplicate-v5.py'),
    (1, './01-connect-success.py'),
    (1, './01-connect-success-v5.py'),
    (1, './01-connect-disconnect-v5.py'),
    (1, './01-connect-invalid-protonum.py'),
    (1, './01-connect-invalid-id-0.py'),
    (1, './01-connect-invalid-id-0-311.py'),
    (1, './01-connect-invalid-id-missing.py'),
    (1, './01-connect-invalid-reserved.py'),
    (1, './01-connect-invalid-id-utf8.py'),
    (1, './01-connect-anon-denied.py'),
    (1, './01-connect-uname-no-password-denied.py'),
    (1, './01-connect-uname-password-denied.py'),
    (1, './01-connect-uname-password-success.py'),
    (1, './01-connect-uname-no-flag.py'),
    (1, './01-connect-uname-pwd-no-flag.py'),
    (1, './01-connect-uname-invalid-utf8.py'),

    (1, './02-subscribe-qos0.py'),
    (1, './02-subscribe-qos1.py'),
    (1, './02-subscribe-qos2.py'),
    (1, './02-subpub-qos0.py'),
    (1, './02-subpub-qos1.py'),
    (1, './02-subpub-qos2.py'),
	(1, './02-subpub-qos1-bad-pubrec.py'),
	(1, './02-subpub-qos1-bad-pubcomp.py'),
    (1, './02-subpub-qos2-bad-puback-1.py'),
    (1, './02-subpub-qos2-bad-puback-2.py'),
	(1, './02-subpub-qos2-bad-pubcomp.py'),
    (1, './02-subpub-qos0-v5.py'),
    (1, './02-subpub-qos1-v5.py'),
    (1, './02-subpub-qos2-v5.py'),
    (1, './02-subpub-qos1-message-expiry.py'),
    (1, './02-subpub-qos1-message-expiry-retain.py'),
    (1, './02-subpub-qos1-message-expiry-will.py'),
    (1, './02-subpub-qos1-nolocal.py'),
    (1, './02-subpub-qos0-retain-as-publish.py'),
    (1, './02-subpub-qos0-send-retain.py'),
    (1, './02-subpub-qos0-subscription-id.py'),
    (1, './02-subpub-qos2-receive-maximum-1.py'),
    (1, './02-subpub-qos2-receive-maximum-2.py'),
    (1, './02-subpub-qos2-pubrec-error.py'),
    (1, './02-subpub-qos0-topic-alias.py'),
    (1, './02-subpub-qos0-topic-alias-unknown.py'),
    (1, './02-unsubscribe-qos0.py'),
    (1, './02-unsubscribe-qos1.py'),
    (1, './02-unsubscribe-qos2.py'),
    (1, './02-unsubscribe-qos2-v5.py'),
    (1, './02-unsubscribe-invalid-no-topic.py'),
    (1, './02-unsubscribe-qos2-multiple.py'),
    (1, './02-unsubscribe-qos2-multiple-v5.py'),
    (1, './02-subscribe-invalid-utf8.py'),
    (1, './02-subscribe-persistence-flipflop.py'),
    (1, './02-subhier-crash.py'),

    (1, './03-publish-qos1.py'),
    (1, './03-publish-qos2.py'),
    (1, './03-publish-b2c-disconnect-qos1.py'),
    (1, './03-publish-c2b-disconnect-qos2.py'),
    (1, './03-publish-b2c-disconnect-qos2.py'),
    (1, './03-publish-b2c-qos1-len.py'),
    (1, './03-publish-b2c-qos2-len.py'),
    (1, './03-publish-c2b-qos2-len.py'),
    (1, './03-pattern-matching.py'),
    #(1, './03-publish-qos1-queued-bytes.py'),
    (1, './03-publish-invalid-utf8.py'),
    (1, './03-publish-dollar.py'),
    (1, './03-publish-qos1-retain-disabled.py'),

    (1, './04-retain-qos0.py'),
    (1, './04-retain-qos0-fresh.py'),
    (1, './04-retain-qos0-repeated.py'),
    (1, './04-retain-qos1-qos0.py'),
    (1, './04-retain-qos0-clear.py'),
    (1, './04-retain-upgrade-outgoing-qos.py'),
    (1, './04-retain-check-source.py'),
    (1, './04-retain-check-source-persist.py'),
    (2, './04-retain-check-source-persist-diff-port.py'),

    (1, './05-clean-session-qos1.py'),

    (2, './06-bridge-reconnect-local-out.py'),
    (2, './06-bridge-br2b-disconnect-qos1.py'),
    (2, './06-bridge-br2b-disconnect-qos2.py'),
    (2, './06-bridge-b2br-disconnect-qos1.py'),
    (2, './06-bridge-b2br-disconnect-qos2.py'),
    (2, './06-bridge-fail-persist-resend-qos1.py'),
    (2, './06-bridge-fail-persist-resend-qos2.py'),
    (2, './06-bridge-b2br-remapping.py'),
    (2, './06-bridge-br2b-remapping.py'),
    (3, './06-bridge-per-listener-settings.py'),

    (1, './07-will-qos0.py'),
    (1, './07-will-null.py'),
    (1, './07-will-null-topic.py'),
    (1, './07-will-invalid-utf8.py'),
    (1, './07-will-no-flag.py'),
    (1, './07-will-delay.py'),
    (1, './07-will-delay-recover.py'),
    (1, './07-will-delay-reconnect.py'),

    (2, './08-ssl-connect-no-auth.py'),
    (2, './08-ssl-connect-no-auth-wrong-ca.py'),
    (2, './08-ssl-connect-cert-auth.py'),
    (2, './08-ssl-connect-cert-auth-without.py'),
    (2, './08-ssl-connect-cert-auth-expired.py'),
    (2, './08-ssl-connect-cert-auth-revoked.py'),
    (2, './08-ssl-connect-cert-auth-crl.py'),
    (2, './08-ssl-connect-identity.py'),
    (2, './08-ssl-connect-no-identity.py'),
    (2, './08-ssl-bridge.py'),
    (2, './08-tls-psk-pub.py'),
    (3, './08-tls-psk-bridge.py'),

    (1, './09-acl-empty-file.py'),
    (1, './09-plugin-auth-unpwd-success.py'),
    (1, './09-plugin-auth-unpwd-fail.py'),
    (1, './09-plugin-auth-acl-sub.py'),
    (1, './09-plugin-auth-acl-sub-denied.py'),
    (1, './09-plugin-auth-v2-unpwd-success.py'),
    (1, './09-plugin-auth-v2-unpwd-fail.py'),
    (1, './09-plugin-auth-defer-unpwd-success.py'),
    (1, './09-plugin-auth-defer-unpwd-fail.py'),
    (1, './09-plugin-auth-msg-params.py'),
    (1, './09-plugin-auth-context-params.py'),
	(1, './09-pwfile-parse-invalid.py'),

    (2, './10-listener-mount-point.py'),

    (1, './11-persistent-subscription.py'),

	(1, './12-prop-session-expiry-invalid.py'),
	(1, './12-prop-subpub-payload-format.py'),
	(1, './12-prop-subpub-content-type.py'),
	(1, './12-prop-assigned-client-identifier.py'),
	(1, './12-prop-server-keepalive.py'),
    (1, './12-prop-response-topic.py'),
    (1, './12-prop-response-topic-correlation-data.py'),
    (1, './12-prop-maximum-packet-size-broker.py'),
    (1, './12-prop-maximum-packet-size-connect.py'),
    (1, './12-prop-maximum-packet-size-publish.py'),
    (1, './12-prop-maximum-packet-size-publish-qos1.py'),
    (1, './12-prop-maximum-packet-size-publish-qos2.py'),
    ]

ptest.run_tests(tests)
